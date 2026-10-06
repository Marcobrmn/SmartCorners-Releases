# SmartCorners

A free macOS menu bar app that turns screen corners into shortcuts for everyday tasks. Move the pointer into a corner, wait for the configured delay, and run its assigned action.

**Release candidate:** 0.1.0 · Build 10 · Apple Silicon (M1 or later) · macOS 13 or later · English interface.

Maintained by [Marcobrmn](https://github.com/Marcobrmn). The application source is privately held. This documentation accompanies a binary distribution; see [source availability and licensing](SOURCE_AVAILABILITY.md).

## Contents

- [Features](#features)
- [Screenshot](#screenshot)
- [Installation](#installation)
- [Using SmartCorners](#using-smartcorners)
- [Permissions and privacy](#permissions-and-privacy)
- [Updates](#updates)
- [Troubleshooting](#troubleshooting)
- [Technical details](#technical-details)
- [Testing and security](#testing-and-security)
- [Publication safety gate](#publication-safety-gate)
- [Support](#support)
- [Roadmap](#roadmap)

## Features

- Assign separate actions to the top-left, top-right, bottom-left and bottom-right corners.
- Create, rename, select and delete profiles. One profile is active at a time.
- Enable or disable individual corners.
- Adjust trigger delay and cooldown to reduce accidental activation.
- Choose visual feedback: Liquid Glass, Siri AI, Blue & White, Aurora or Sunset. These are animation styles; “Siri AI” does not connect to Siri or an AI service.
- Pause and resume monitoring from Settings or the menu bar.
- Choose whether to launch at login and check for updates automatically.
- Use onboarding and permission/Apple Hot Corners status checks.

| Action in Settings | What it does | How to configure/use it |
| --- | --- | --- |
| No Action | Performs nothing | Use it for an unused corner, or disable the corner. |
| Open Website | Opens a URL through macOS in its registered handler | Enter a complete address, such as `https://example.com`. |
| Open Application | Opens an installed app | Select an application from the list. |
| Run Shortcut | Runs a named macOS Shortcut | Create it in Shortcuts first, then select it. Its own permissions and effects still apply. |
| Capture Screenshot to Clipboard | Uses macOS screenshot keyboard shortcuts | Choose Full Screen, Select Window or Select Area. For window/area capture, complete the selection; paste the image into another app. |
| Open New Calendar Event | Activates Calendar and sends its new-item shortcut | Enter event details in Calendar yourself. |
| Open New Note | Activates Notes and sends its new-note shortcut | Enter note content in Notes yourself. |

**Focus mode is planned, not functional in this release.** Existing legacy Focus assignments remain saved and are shown as unavailable. They cannot be enabled until replaced by a supported action. Legacy Calendar titles and Notes text are also preserved for compatibility but are not inserted into the new item.

The monitor checks corners across connected displays using the active profile. Display-change behavior is implemented; comprehensive testing of every multi-display arrangement has not been recorded.

## Screenshot

**Development preview: private Build 15, not the public Build-10 download.** These genuine screenshots were captured from the installed English Build 15 on October 6, 2026. They show active monitoring without a permission warning. No personal information or UI content was edited into the images.

![SmartCorners private Build 15: active profile and corner actions](screenshots/smartcorners-0.1.0-build-15-settings-dark.jpg)

![SmartCorners private Build 15: corner actions, delay, cooldown and animation style](screenshots/smartcorners-0.1.0-build-15-corners-and-timing-dark.jpg)

## Installation

Download the versioned DMG from [SmartCorners Releases](https://github.com/Marcobrmn/SmartCorners-Releases/releases).

### Distribution and trust

**This independently developed GitHub build has no Apple Developer ID signature and is not notarized.** Its ad-hoc signatures check internal consistency, and Sparkle update archives have an EdDSA signature. Neither establishes Apple-verified developer identity or Gatekeeper approval. Opening a blocked app creates a security exception: proceed only if you trust the source. Development ownership and checksums are not proof that software is free of vulnerabilities.

1. Download the versioned DMG and compare its SHA-256 with the release notes or `SHA256SUMS.txt`.
2. Open the DMG in Finder, then drag **SmartCorners.app** into **Applications**. If replacing an older copy, quit it first.
3. Eject the DMG and open SmartCorners from Applications. Keep one installed copy to avoid confusion between builds or permission entries.
4. If macOS blocks opening and you trust the source, go to **System Settings → Privacy & Security** and choose **Open Anyway** for SmartCorners when offered. Review and confirm the subsequent prompt. See [Apple's opening instructions](https://support.apple.com/en-us/102445). Wording and availability vary by macOS version and management policy.

Do not disable Gatekeeper globally or remove quarantine as the normal installation procedure. The owner reported a successful initial installation, but its exact dialogs were not recorded. A clean-account quarantined first launch of the final Build-10 DMG is still unrecorded; the procedure above is Apple's documented path, not a claim that every Mac will show the same prompts.

To calculate a downloaded file's checksum in Terminal:

```sh
shasum -a 256 ~/Downloads/SmartCorners-0.1.0-build.10-github-non-notarized-17435d3db15f.dmg
```

Expected SHA-256: `af969aaaf14626f16a4fa1a82b86b9578ea30d2d7e9fc2208493e24ca0680810`.

## Using SmartCorners

### First launch

1. Read the welcome screen. Choose the offered setup preferences and review permission status.
2. Enable **Launch at Login** only if you want SmartCorners to start when you sign in. macOS may require approval in Login Items.
3. If using screenshot, Calendar or Notes actions, use the permission button to open macOS Accessibility settings and grant access to the installed SmartCorners app.
4. Review any existing Apple Hot Corners. The optional **Disable Apple Hot Corners** button changes all four system corner assignments and their modifiers and restarts the Dock. Only use it if you want that system change; it is not required to store a profile.
5. Choose **Start Using SmartCorners**, then configure corners in the main Settings window.

### Configure a profile

1. Open **Settings** from the menu bar.
2. Select a profile in the sidebar. Use **+** to add one, edit **Name** to rename it, or **−** to delete the selected profile. The last profile cannot be deleted.
3. For each corner, select an action and its options. Use **Active/Disabled** to control that corner.
4. Adjust **Delay**, **Cooldown** and **Animation Style**. Many controls save changes immediately; **Save** also persists the current configuration.
5. Move the pointer into an enabled corner and hold it for the delay. Move away and back to trigger again; the cooldown limits repeated actions.

**Pause** stops monitoring. Saving, resetting a profile or reopening Settings preserves a deliberate pause; only **Enable** resumes it. The pause state is saved for the next app launch. **Reset Profile** restores the active profile's default corner assignments; it does not erase every profile or revoke permissions.

### Menu bar and general settings

| Control | Purpose |
| --- | --- |
| Open Settings | Opens profiles and corner configuration. |
| Pause SmartCorners / Enable SmartCorners | Stops or resumes monitoring. A paused icon is marked and accompanied by “paused”. |
| Check for Updates… | Opens the Sparkle update flow. |
| Quit | Stops and exits the app. Closing the Settings window alone leaves the menu bar app running. |
| Settings toolbar button | Opens general settings, login preferences, update preferences and permission checks. |
| Refresh Status | Rechecks the current permission and system-corner status. |
| Show Welcome Again | Reopens onboarding without deleting profiles. |
| Report → Open on GitHub | Opens a browser draft for a Bug or Feature Request with your title/details, app version/build and macOS version. A GitHub account is needed to submit it; nothing is posted automatically. |
| Copy Report | Copies the draft locally without a GitHub account. For long reports, open the GitHub issues page and paste it into a new issue. |

## Permissions and privacy

SmartCorners has no analytics backend, app account or telemetry upload. Profiles and onboarding state stay on your Mac. See [Privacy](PRIVACY.md) for storage, network access, logs and deletion details.

- **Accessibility:** screenshot, Calendar and Notes actions send keyboard events. This is a powerful permission; grant it only if you trust the app. Basic corner detection reads pointer position and does not record keystrokes.
- **Shortcuts:** the selected shortcut may ask for its own permissions or access the network. SmartCorners does not restrict what that shortcut does.
- **Other macOS prompts:** opened apps and workflows may require their own approvals. SmartCorners does not directly read Calendar or Notes databases.

Screenshots are copied to the local clipboard, not uploaded by SmartCorners. Clipboard managers, Universal Clipboard and applications you paste into can handle that data independently.

## Updates

Sparkle checks the GitHub-hosted update feed and installs compatible signed archives. You can check manually from the menu bar or general settings and control automatic checking in Settings.

The production appcast is currently empty, so this first public release is available as a manual download. A private update to Build 9 passed; a private A→B update using this exact Build-10 archive has not been performed and remains unverified. The earlier result is not claimed as a test of Build 10.

In Build 10, checking for updates dismisses SmartCorners Settings windows even when no newer version exists. The menu bar app and monitoring continue running. Installing an update closes the app and relaunches it. Avoid launching another copy during the update.

## Troubleshooting

- **No corner action:** check that SmartCorners and the individual corner are enabled, verify the active profile, then wait for the configured delay. Existing Apple Hot Corners can interfere.
- **Screenshot/Calendar/Notes action does not work:** review Accessibility access for the installed copy, click Refresh Status and quit/reopen the app if the status remains stale. These actions depend on standard macOS keyboard shortcuts and app behavior.
- **No application or Shortcut in the list:** make sure it is installed or created first, then reopen Settings. SmartCorners does not install selected apps or create shortcuts.
- **Corrupt configuration warning:** monitoring remains stopped and the original file is preserved. Review the recovery controls before choosing defaults; recovery keeps a copy of the unreadable file. Do not treat Reset Profile as corruption recovery.
- **Already on the latest version:** verify the version/build in the menu bar and that you started the intended Applications copy. The production feed currently has no update entries; download the release manually if needed.
- **Want to remove the app:** disable Launch at Login, quit SmartCorners and move the app to the Trash. This does not guarantee removal of settings, backups or macOS permission entries. See [Privacy](PRIVACY.md#removing-local-data). An in-app removal-preparation feature is planned.

## Technical details

No Homebrew package, Python runtime, Node.js runtime or additional app is installed by the DMG. The app bundle includes its executable, resources and Sparkle framework/helpers. macOS supplies the system APIs and command-line tools below.

| Component | Purpose | Installed by SmartCorners? |
| --- | --- | --- |
| Swift / SwiftUI / AppKit / Foundation | Native app, menu bar, windows and local configuration | Compiled app plus macOS system frameworks; no separate user installation. |
| ApplicationServices / Core Graphics | Accessibility checks and generated keyboard events | System frameworks already in macOS. |
| ServiceManagement (`SMAppService.mainApp`) | Optional launch-at-login registration | System API; registers this app when enabled, not a custom daemon. |
| Sparkle **2.10.0** | Update discovery, download, installation and relaunch | Embedded third-party framework and helpers inside the app bundle. |
| `/usr/bin/shortcuts` | Lists/runs your named Shortcuts | macOS tool; invoked only for list/run operations. |
| `/usr/bin/defaults`, `/usr/bin/killall Dock` | Optional disabling of Apple Hot Corners | macOS tools; used for that explicit setting change. |
| Browser, selected apps, Notes and Calendar | Handles requested actions and reports | Existing apps are opened; none is installed by SmartCorners. |

The selected Build-10 runtime uses consistent ad-hoc signing without the Hardened Runtime option, so Sparkle can load under this distribution mode. This is a packaging choice, not a claim of equivalent protection to a Developer-ID release.

While enabled, the app checks pointer position approximately every 40 ms and manages temporary visual overlays. It does not install a custom privileged helper, kernel extension or independent always-running monitoring service. Sparkle uses bundled **Updater.app**, **Autoupdate**, **Downloader.xpc** and **Installer.xpc** during its update workflow; they are not separate products you must install manually.

Configuration: `~/Library/Application Support/SmartCorners/SmartCorners.json`. macOS defaults domain and bundle ID: `app.smartcorners.SmartCorners`. Version 0.1.0, build 10; app source commit `17435d3db15ffd6718e44794d8984bd1a2007010`. For full component and license information, see [third-party notices](THIRD_PARTY_NOTICES/Sparkle-LICENSE.txt).

## Testing and security

For Build 10, Swift regression tests, 12 structure checks, release compilation, mounted-DMG inspection, bundle identity and nested signature checks, and archive signature verification passed. English updater language selection passed under a German preference. The GitHub report draft and Copy Report flow were tested in a normal interactive macOS session without submitting an issue. Earlier owner-reported onboarding/permission and Build-9 automatic-update results remain historical; they are not a claim of comprehensive Build-10 acceptance.

These are development and release checks, **not an independent security audit or penetration test**. No claim is made that SmartCorners is vulnerability-free. The final clean-account quarantined first launch, exact Gatekeeper dialogs, comprehensive action/login/light-and-dark acceptance and deferred update-failure cases are not all recorded as passed. See the [release notes](RELEASE_NOTES_0.1.0.md) for this candidate's evidence and limits.

Security issues and disclosure instructions are documented in [SECURITY.md](SECURITY.md).

## Publication safety gate

The `publication-safety` GitHub Actions check runs on pull requests and pushes to `main`. It scans tracked repository files (including binary bytes) for local home/build paths and internal IPs, and reachable Git history with Gitleaks for secret patterns. A failed or incomplete check fails; branch protection must require `publication-safety` to make it a mandatory merge gate. Matches are withheld from public logs and require private human review.

**Direct GitHub Release asset uploads are NOT gated by this workflow.** The published DMG is a release asset, not a tracked file; this check neither scans nor changes the existing DMG. Before any future asset upload, separately inspect the exact artifact and approve publication. This gate does not replace independent release review.

## Support

For bugs or feature requests, use [SmartCorners Issues](https://github.com/Marcobrmn/SmartCorners-Releases/issues). Include the app version/build, macOS version, expected behavior and reproduction steps. Remove personal URLs, shortcut names, screenshots and other private information before sharing. Read [CONTRIBUTING.md](CONTRIBUTING.md) for reporting guidance. Response times and future release dates are not guaranteed.

## Roadmap

Planned improvements; no promised release dates. Priorities may change based on testing and feedback.

- [ ] Focus mode actions once the macOS integration works reliably.
- [ ] Removal preparation: delete app settings/profiles, disable launch at login and help revoke permissions, with macOS limitations stated clearly.
- [ ] Smoother update checks while Settings is open.
- [ ] Review language support and consider an English-only interface.
