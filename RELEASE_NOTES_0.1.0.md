# SmartCorners 0.1.0 — Build 10

Free binary release for **Apple Silicon (M1 or later)** and **macOS 13 or later**, with an English interface. The application source remains privately held.

## Features

Assign supported actions to four screen corners, create profiles, adjust delay/cooldown, choose visual feedback, and pause from the menu bar. Open websites or applications, run macOS Shortcuts, capture screenshots to the clipboard, or open a blank Notes note or Calendar event. See the [README](README.md) for setup and action limits.

Build 10 replaces email reports with **Open on GitHub** for Bug and Feature Request drafts, adds local **Copy Report**, includes app/build/macOS versions, and keeps submission under your control. A GitHub account is required to submit an issue. Long reports remain copyable for manual pasting; no reporting token or email address is embedded in the app.

Focus actions are planned for a later release. Legacy Focus rules remain stored but unavailable until replaced with a supported action. Saving/resetting/reopening Settings preserves a deliberate pause. Corrupt configuration stops monitoring and preserves the original file.

## Installation and trust

**This independently developed build has no Apple Developer ID signature and is not notarized.** Ad-hoc signing and Sparkle EdDSA update signatures do not establish Apple-verified identity or Gatekeeper approval. A manual opening exception lets software run without that Apple verification; proceed only if you trust the source.

Open the DMG in Finder and drag SmartCorners into Applications. Quit an older copy before replacing it. If macOS blocks opening and you trust the download, use System Settings → Privacy & Security → **Open Anyway** for SmartCorners when offered, then review the prompt. See [Apple's instructions](https://support.apple.com/en-us/102445). Dialogs and availability vary across macOS versions and management policies. Do not disable Gatekeeper globally or remove quarantine as the standard installation method.

## Artifact

- File: `SmartCorners-0.1.0-build.10-github-non-notarized-17435d3db15f.dmg`
- Size: **2,720,079 bytes**
- SHA-256: `af969aaaf14626f16a4fa1a82b86b9578ea30d2d7e9fc2208493e24ca0680810`
- App: `app.smartcorners.SmartCorners`, version `0.1.0`, build `10`
- Source commit: `17435d3db15ffd6718e44794d8984bd1a2007010`

## Validation and known behavior

Build-10 Swift tests passed: 13 XCTest cases and 8 Swift Testing regression cases, zero failures. All 12 structure checks, release compilation, English bundle language selection under a German preference (with negative control), mounted-DMG identity inspection, nested ad-hoc signature checks and final archive EdDSA verification passed. A normal interactive macOS test confirmed a correctly prefilled GitHub Feature Request draft and Copy Report; no test issue was posted.

Checking for updates dismisses Settings windows even when no newer version exists; the menu bar app continues running. The earlier private update to Build 9 passed with automatic relaunch. **An A→B update using this exact Build-10 archive is unverified.** The production appcast stays empty for now; this release is available by manual download.

The owner reported successful earlier installation, onboarding and permissions tests, but exact first-launch Gatekeeper dialogs were not recorded. A clean-account quarantined first launch of this final Build-10 DMG, comprehensive action/login/light-and-dark acceptance, and deferred update-failure cases are not recorded as passed. A replacement final-build screenshot is pending. These development checks are not an independent security audit, penetration test or vulnerability-free guarantee.


## Maintainer follow-up — October 6, 2026

The current Build-10 executable retains absolute build-machine paths in debug symbol records. A packaging correction removes these records before final signing in a future build. The released DMG has not been modified or silently replaced. Current README images are clearly labeled as private Build-15 development previews, not screenshots of the public Build-10 download.
