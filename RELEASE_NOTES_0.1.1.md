# SmartCorners 0.1.1 — Build 17

Apple Silicon (M1 or later) · macOS 13 or later · English interface

## Changes

- Smoother scrolling in Settings and less unnecessary background work.
- Animation previews run on hover; corner feedback respects Reduce Motion.
- A separate **SmartCorners Actions** helper handles screenshot, Calendar and Notes actions. Its Accessibility permission can remain in place across main-app updates when the helper is unchanged.
- Clearer permission instructions.

## Installing or upgrading

Quit SmartCorners, open the new DMG in Finder and drag the app into Applications. When upgrading from 0.1.0, grant **SmartCorners Actions** Accessibility access once; the main app’s previous grant does not transfer.

This build is **not signed with an Apple Developer ID and is not notarized**. Follow the [installation guide](README.md#installation) if macOS blocks the first launch.

This version is a manual download; the update feed has no published updates.

## Known limitations

- Focus mode is not available.
- Calendar and Notes actions open blank items without predefined text.
- Checking for updates closes Settings; the menu bar app keeps running.

The download checksum is in [SHA256SUMS.txt](SHA256SUMS.txt).
