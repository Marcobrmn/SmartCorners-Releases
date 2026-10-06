"""Synthetic canaries only; no live credentials or private addresses."""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from publication_safety import categories

SCRIPT = Path(__file__).with_name("publication_safety.py")


class PublicationSafetyTests(unittest.TestCase):
    def test_text_and_binary_canaries(self):
        examples = (
            b"/Users/" + b"sample/Library/Developer/Xcode/DerivedData/demo",
            b"/home/" + b"builder/work/project",
            b"/private/var/folders/" + b"aa/build-cache",
            b"C:\\Users\\" + b"sample\\AppData\\build\\thing",
            b"connect 192.168." + b"4.5",
            b"connect 172.20." + b"1.2",
            b"connect 10." + b"1.2.3",
            b"connect fd12:" + b":1",
        )
        for value in examples:
            with self.subTest(canary_type="synthetic", encoding="bytes"):
                self.assertTrue(categories(b"\x00BIN\x00" + value + b"\x00"))
            with self.subTest(canary_type="synthetic", encoding="utf16"):
                self.assertTrue(categories(value.decode().encode("utf-16-le")))

    def test_public_addresses_relative_paths_and_docs(self):
        self.assertEqual(categories(b"docs/build/output public 8.8.8.8 and 203.0.113.2; ~/Library"), set())

    def test_git_tracked_and_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            subprocess.run(["git", "init", "-q", str(repo)], check=True, stdout=subprocess.DEVNULL)
            item = repo / "payload.bin"
            item.write_bytes(b"safe")
            subprocess.run(["git", "-C", str(repo), "add", "payload.bin"], check=True)

            def scan():
                return subprocess.run([sys.executable, str(SCRIPT)], cwd=repo, capture_output=True, text=True)

            self.assertEqual(scan().returncode, 0)
            item.write_bytes(b"\x00internal 192.168." + b"7.9\x00")
            result = scan()
            self.assertEqual(result.returncode, 1)
            self.assertNotIn("192.168." + "7.9", result.stdout + result.stderr)
            item.unlink()
            self.assertEqual(scan().returncode, 2)


if __name__ == "__main__":
    unittest.main()
