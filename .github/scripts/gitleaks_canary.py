#!/usr/bin/env python3
"""Fail closed if the pinned Gitleaks binary cannot detect a synthetic token."""

import json
import os
import secrets
import string
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> int:
    try:
        executable = os.environ["GITLEAKS_BIN"]
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            root = base / "repo"
            root.mkdir()
            config = base / "trusted.toml"
            config.write_text("[extend]\nuseDefault = true\n")
            ignore = base / "empty.ignore"
            ignore.write_text("")
            token = "ghp_" + "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(36))
            (root / "canary.txt").write_text("token = " + token + " # gitleaks:allow\n")
            (root / ".gitleaks.toml").write_text("title='disabled'\n")
            subprocess.run(["git", "init", "-q", str(root)], check=True, capture_output=True)
            subprocess.run(["git", "-C", str(root), "add", "canary.txt", ".gitleaks.toml"], check=True, capture_output=True)
            subprocess.run(["git", "-C", str(root), "-c", "user.name=Canary", "-c", "user.email=canary@example.invalid", "commit", "-qm", "synthetic"], check=True, capture_output=True)
            for mode in ("dir", "git"):
                report = root / (mode + ".json")
                result = subprocess.run(
                    [executable, mode, "--no-banner", "--redact=100", "--log-level", "error",
                     "--config", str(config), "--gitleaks-ignore-path", str(ignore),
                     "--ignore-gitleaks-allow", "--report-format", "json", "--report-path", str(report), str(root)],
                    capture_output=True, timeout=30, check=False,
                )
                if result.returncode != 1 or not report.exists() or not json.loads(report.read_text()):
                    raise RuntimeError("canary not detected")
        print("Gitleaks synthetic detection passed; values withheld.")
        return 0
    except (OSError, KeyError, ValueError, RuntimeError, subprocess.SubprocessError):
        print("Gitleaks synthetic detection failed closed; values withheld.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
