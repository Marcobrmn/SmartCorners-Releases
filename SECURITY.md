# Security policy

## Scope and support

The current release is SmartCorners 0.1.0 Build 10. Older private test builds are superseded and should not be used as the distribution candidate. No fixed security-support period or response deadline is promised.

## Reporting a vulnerability

Do not publish exploit details, credentials or personal data in a public issue. On the distribution repository's Security tab, use **Report a vulnerability** if private vulnerability reporting is available. Its availability is not asserted by this document.

If that option is absent, open an issue containing only a request for a private security contact. Wait for the maintainer to arrange a private channel before sending sensitive details. The in-app Report function opens a public GitHub issue draft and is not a private security channel.

A useful private report includes the app version/build, macOS version, affected component, reproduction steps and impact. Share only the minimum data needed. Do not attach signing keys or complete personal configuration files.

## Verification and limitations

Development regression and release-integrity checks have been performed. No independent security audit, penetration test or vulnerability-free guarantee is claimed. Archive checksums and Sparkle EdDSA signatures help verify artifact integrity but are not an audit of application behavior. See [testing and security](README.md#testing-and-security), [release notes](RELEASE_NOTES_0.1.0.md) and [distribution trust](README.md#distribution-and-trust).

Third-party code: Sparkle 2.10.0 is pinned and bundled. macOS frameworks/tools are supplied by Apple. Changes to dependencies must be reviewed and revalidated for future builds.
