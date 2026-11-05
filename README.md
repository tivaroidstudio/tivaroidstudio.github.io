# Tivaroid Studio — portfolio

Public site: https://tivaroidstudio.github.io/

## Add or publish an app

Edit only `apps.js`. Each item supports `id`, `name`, `category`, `status` (`live`, `soon`, or `development`), `symbol`, `description`, `play`, `privacy`, and optional `deletion`. Add a new object to the array to publish another card.

For an app in development, set `status: "development"` and do not add a Google Play link until it is published. For a production app, set `status: "live"`, add the verified Google Play URL and publish an accurate privacy policy at a stable URL before adding its `privacy` link. Do not invent policy statements; check the actual app permissions, SDKs, data flows and Google Play Data safety disclosures.

## Important existing links

- `/app-ads.txt` remains in the domain root and must not be moved.
- `/hangman-rivals-privacy/index.html` preserves the existing Hangman privacy policy.
- `/delete-account.html` preserves the existing Hangman account deletion flow.
- The old root privacy URL now serves the portfolio; if that root URL was entered in Play Console, update it to the dedicated privacy URL immediately.

AllRemote is marked as published, but its privacy URL is intentionally left blank until the approved policy is moved or verified. The same applies to future apps; don't link a placeholder policy as if it were complete.

This is a static GitHub Pages site with no backend, analytics or cookies added by the portfolio.

## TivaroSQL Studio

The in-development TivaroSQL Studio entry is maintained in `apps.js`. Its public English privacy policy is at `/tivarosqlstudio-privacy/index.html`. Before releasing to Google Play, recheck the published policy against the shipping app build, permissions, SDKs, security settings and Data safety disclosures.
