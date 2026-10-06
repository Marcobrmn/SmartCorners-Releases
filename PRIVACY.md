# Privacy

Last updated: October 6, 2026.

SmartCorners has no app accounts, analytics backend or telemetry upload. Its profiles are stored locally. For installation and distribution trust, read the [README](README.md#distribution-and-trust).

## Local data

`~/Library/Application Support/SmartCorners/SmartCorners.json` stores profiles, assignments, preferences, pause and onboarding state. Sparkle preferences and window state may also reside in the macOS defaults domain `app.smartcorners.SmartCorners`. Recovery copies and manually created reset backups remain on the Mac until removed. These files may contain personal website addresses, app paths and Shortcut names. SmartCorners does not upload them.

The app reads pointer position while monitoring, discovers installed app names/icons and lists Shortcuts for configuration. It does not record typed keys. Action failures may be written to local macOS logs; errors can contain configured values or paths. Review logs before sharing them.

The action helper uses `~/Library/Application Support/SmartCorners-Actions/` for restricted local communication and, where present, cached public authorization. Release authorization is signed public metadata bundled with the official app; it contains code identity, not your profiles or a private key. No authorization server is required.

## Network access

Sparkle contacts the GitHub-hosted update feed for manual checks or automatic checks according to update preferences, and downloads updates when requested or permitted by those preferences. GitHub may process connection metadata under [its privacy policy](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). No profile upload is required.

Website actions open a URL in its registered handler. Browsers, launched apps and Shortcuts may make their own network requests, store data or synchronize it. SmartCorners does not control those services.

## Permissions and system changes

The bundled SmartCorners Actions helper performs screenshot, Calendar and Notes actions using generated keyboard events and require Accessibility access. This grants powerful interaction capabilities; only grant it if you trust the app. SmartCorners opens the system apps and uses their shortcuts rather than directly reading their databases. A chosen Shortcut may need additional permissions.

Screenshots go to the local clipboard. SmartCorners does not upload them; clipboard managers, Universal Clipboard and destination apps can process them separately. No separate capture database is maintained by SmartCorners.

Launch at Login registers the app through macOS ServiceManagement only when enabled. The explicit Disable Apple Hot Corners action alters Dock corner/modifier preferences and restarts the Dock. It does not preserve a restorable history of the previous Apple corner assignments.

## Reports

Report prepares a Bug or Feature Request from your title/details and the app/macOS versions. Copy Report writes that text to the local clipboard. Open on GitHub passes it in the browser URL to GitHub as an issue draft; it may appear in browser history and connection records even before submission. Review the draft in your browser and submit it yourself using a GitHub account. Nothing is posted automatically and no configuration or logs are attached. GitHub issues in the distribution repository are public; do not include secrets or personal data. Long reports can be copied and pasted into GitHub manually. Use [the security policy](SECURITY.md) for vulnerabilities.

## Removing local data

Disable Launch at Login and quit every SmartCorners copy before removing the app or its local data. Moving the app to the Trash alone does not promise deletion of profiles, defaults, updater cache, backup files or permission entries.

To remove saved profiles, use Finder → Go → Go to Folder to inspect `~/Library/Application Support/SmartCorners/` and delete it only after deciding whether to retain a backup. Also inspect `~/Library/Application Support/SmartCorners-Actions/` after quitting the helper. Separately review any `SmartCorners-settings-backups` directory and app preferences. macOS permissions must be reviewed in System Settings → Privacy & Security; removing files is not a guarantee of revoked grants. There is no in-app complete-cleanup function in this release.

## Contact

Use [SmartCorners Issues](https://github.com/Marcobrmn/SmartCorners-Releases/issues) for general privacy questions without publishing personal data. For sensitive concerns, request a private contact first as described in [SECURITY.md](SECURITY.md).
