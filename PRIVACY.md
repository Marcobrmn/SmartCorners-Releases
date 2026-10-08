# Privacy

SmartCorners has no app accounts, analytics or telemetry uploads. Profiles and settings stay on your Mac.

## Local data

Profiles, corner assignments, preferences and onboarding state are stored in:

```text
~/Library/Application Support/SmartCorners/SmartCorners.json
```

This file can contain website addresses, application paths and Shortcut names. The action helper uses `~/Library/Application Support/SmartCorners-Actions/` for local communication. App and updater preferences use the macOS defaults domain `app.smartcorners.SmartCorners`. Recovery copies and manually created backups remain on your Mac until you remove them.

SmartCorners reads pointer position to detect corners and lists installed apps and Shortcuts for configuration. It does not record typed keys. Action errors may appear in local macOS logs; review logs for personal values before sharing them.

## Network access

Update checks contact the GitHub-hosted update feed and downloads come from GitHub. GitHub handles connection data under [its privacy policy](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). SmartCorners does not upload profiles.

Websites, applications and Shortcuts you launch may make their own network requests or synchronize data.

## Permissions and system changes

**SmartCorners Actions** needs Accessibility access to send keyboard commands for screenshots, Calendar and Notes. SmartCorners opens those apps rather than reading their databases directly. Shortcuts may require permissions of their own.

Screenshots are copied to the clipboard. SmartCorners does not upload them. Clipboard managers, Universal Clipboard and apps you paste into may process them separately.

**Launch at Login** registers the app to start when you sign in. **Disable Apple Hot Corners** clears the four macOS corner assignments and their modifiers, then restarts the Dock. Previous assignments are not backed up for automatic restoration.

## Bug and feature reports

**Copy Report** copies your report to the local clipboard. **Open on GitHub** sends the report title, details and app/macOS versions to GitHub in a browser URL to create an issue draft. That URL may appear in browser history. No report is submitted automatically, and no configuration or logs are attached.

GitHub issues are public. Review the draft and remove personal information before submitting. For sensitive security reports, use [SECURITY.md](SECURITY.md).

## Removing local data

1. Disable **Launch at Login**, then quit SmartCorners and its action helper.
2. Move SmartCorners from Applications to the Trash.
3. In Finder, use **Go → Go to Folder** to inspect `~/Library/Application Support/SmartCorners/`. Back up any profiles you want to keep, then delete the folder to remove them.
4. Remove `~/Library/Application Support/SmartCorners-Actions/` if you no longer use the helper. Review any `SmartCorners-settings-backups` folder separately.
5. Review Accessibility entries in **System Settings → Privacy & Security** and remove access you no longer need.

Moving the app to the Trash does not remove saved profiles, preferences, updater caches, backups or permission entries.

## Questions

Use [Issues](https://github.com/Marcobrmn/SmartCorners-Releases/issues) for general privacy questions without posting personal data. Request a private contact for sensitive concerns.
