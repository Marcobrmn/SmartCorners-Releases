#!/usr/bin/env python3
"""Fail closed on local paths and non-public IPs in git-tracked file bytes."""

import ipaddress
import re
import subprocess
import sys
from pathlib import Path

# Require an identifiable path component; ordinary relative paths are allowed.
LOCAL_PATH = re.compile(
    rb"(?<![\w./])(?:/(?:Users|home|builds|build|workspace|DerivedData)/[\w.-][^\s/\\]*"
    rb"|/(?:private/)?(?:tmp|var/tmp|var/folders)/[\w.-][^\s/\\]*"
    rb"|/Volumes/[\w.-][^\s/\\]*/(?:build|Build|DerivedData)/[\w.-][^\s/\\]*)"
    rb"|[A-Za-z]:\\(?:Users|[^\s\\]+\\(?:build|Build|DerivedData))\\[^\s\\]+"
)
IPV4 = re.compile(rb"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])")
IPV6 = re.compile(rb"(?<![\w:])(?:[0-9A-Fa-f]*:[0-9A-Fa-f:]+)(?![\w:])")
PRIVATE_V4 = tuple(ipaddress.IPv4Network((address, prefix)) for address, prefix in (
    (0x0A000000, 8), (0xAC100000, 12), (0xC0A80000, 16),
    (0x7F000000, 8), (0xA9FE0000, 16),
))
PRIVATE_V6 = tuple(ipaddress.IPv6Network((address, prefix)) for address, prefix in (
    (0xFC00 << 112, 7), (0xFE80 << 112, 10), (1, 128),
))


def categories(data: bytes) -> set[str]:
    # Raw bytes catch ASCII embedded in binaries; decoded variants catch UTF-16 strings.
    variants = [data]
    for encoding in ("utf-16-le", "utf-16-be"):
        variants.append(data.decode(encoding, errors="ignore").encode("utf-8"))
    found = set()
    for value in variants:
        if LOCAL_PATH.search(value):
            found.add("local-path")
        for pattern, networks in ((IPV4, PRIVATE_V4), (IPV6, PRIVATE_V6)):
            for match in pattern.finditer(value):
                try:
                    address = ipaddress.ip_address(match.group().decode("ascii"))
                except ValueError:
                    continue
                if any(address in network for network in networks):
                    found.add("internal-ip")
    return found


def main() -> int:
    try:
        names = subprocess.run(
            ["git", "ls-files", "--cached", "-z"], check=True, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        ).stdout.split(b"\0")
        if not names or names == [b""]:
            raise RuntimeError("no tracked files")
        findings = set()
        for name in names:
            if not name:
                continue
            path = Path(name.decode(errors="surrogateescape"))
            # Symlinks are scanned as link text, never followed outside the checkout.
            if path.is_symlink():
                data = path.readlink().as_posix().encode("utf-8", errors="surrogateescape")
            else:
                data = path.read_bytes()
            findings.update(categories(data))
        if findings:
            print("Publication safety failed: tracked content contains " + ", ".join(sorted(findings)) + ". Values withheld.")
            return 1
        print("Publication safety passed: tracked content contains no targeted local paths or internal IPs.")
        return 0
    except (OSError, RuntimeError, subprocess.CalledProcessError, UnicodeError) as exc:
        # Avoid printing exception text: it could contain sensitive path material.
        print("Publication safety failed closed: tracked-file scan could not complete.")
        return 2


if __name__ == "__main__":
    sys.exit(main())
