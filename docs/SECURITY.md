# Security and autonomy

## Secrets
- Commit placeholders only. Never commit .env, OAuth client secrets, refresh/access tokens, API keys, service-role keys, or passwords.
- Use GitHub Actions secrets or a deployment secret manager.
- Rotate any exposed credential; removing a commit does not revoke it.
- Never log tokens, authorization headers, or signed URLs.

## Authorization
- Request least-privilege OAuth scopes and explain them.
- Enforce workspace/channel ownership on every operation.
- Encrypt provider credentials at rest; decrypt only server-side.
- Audit grants, revocations, and external actions.

## Autonomy boundaries
- Default publishing mode: approval_required.
- Enable automated publishing only after explicit channel-owner authorization with channel scope, content rules, schedule limits, and spend caps.
- Require confirmation for deletion, visibility changes, channel settings, and spending.
- Provide a pause/kill switch and per-workspace budgets.
- Never guarantee rankings, views, subscribers, or revenue.

## Content integrity
Respect copyright, licenses, YouTube policies, privacy, and law. Do not copy creator scripts or imitate a living creator's voice without authorization. Track asset provenance, verify factual claims, and avoid spam, misleading metadata, artificial engagement, and mass repetitive uploads.

## Operations
Rate-limit and honor YouTube quotas. Validate media before upload. Reconcile upload status before retrying. Audit approvals, publishing, spending, credential changes, and destructive actions.
