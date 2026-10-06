# SmartCorners 0.1.1 — Build 17

## Changes

- A bundled, stable SmartCorners Actions helper handles screenshot, Notes and Calendar actions. Main-app updates can preserve its Accessibility grant while its identity remains unchanged. On upgrading from an earlier version, grant **SmartCorners Actions** once; the main app's old grant does not transfer.
- Action authorization works from signed public metadata in the official DMG without an authorization server.
- Smoother Settings scrolling: unchanged monitor state no longer causes repeated redraws or permission checks. Preview animations run on hover while active; edge feedback respects Reduce Motion.
- Release executables have local build-machine debug paths stripped before signing.
- Clearer permission instructions and updated English documentation.

## Installation

Download this release's versioned DMG and use Finder to copy SmartCorners into Applications. Required authorization metadata is preserved by the official installation route. See [the installation guide](README.md#installation) for manual opening instructions and the security trade-off.

This build has **no Apple Developer ID signature and is not notarized**. Ad-hoc code checks and the Sparkle EdDSA archive signature do not establish Apple developer identity or Gatekeeper approval.

The production update feed remains empty; this release is a manual download.

## Validation and limits

30 Swift tests, 12 structure checks, release compilation, English updater selection under a German preference, mounted-DMG inspection, ad-hoc component checks and independent final-archive EdDSA verification passed. The exact archive's update/relaunch result and genuine screenshots are recorded with this release. The owner confirmed the offered actions and smoother scrolling.

Clean-account first launch with normal download quarantine, exact Gatekeeper dialogs, comprehensive login/light-and-dark acceptance and update-failure cases are not fully recorded. Development testing is not an independent security audit. Performance depends on use; no battery-life guarantee is made.

App identity, source revision, archive size, SHA-256 and public update signature are in [MANIFEST.json](MANIFEST.json). Source code is not publicly available.
