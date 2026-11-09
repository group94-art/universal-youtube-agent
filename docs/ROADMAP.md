# Roadmap

## Phase 0 — foundation
Public repo, secret template, architecture/security docs, FastAPI shell, skill catalog, health endpoint, initial tests.

## Phase 1 — secure core (in progress)
Tenant-aware workspace, membership, channel, task, task-event and audit-event models; PostgreSQL migration; typed settings; deterministic task state machine; CI test workflow. Authentication, membership enforcement, credential vault and production RLS remain required before public deployment.

## Phase 2 — YouTube connectivity
OAuth consent/callback, channel discovery, token refresh/revocation, quota-aware reads, analytics sync, approval-required upload workflow.

## Phase 3 — research and planning
Provider adapters, source provenance, channel audit, strategy, calendar, automated tests with fixtures.

## Phase 4 — creative and media
Script/storyboard, voice and visual adapters, FFmpeg assembly, captions, thumbnails, asset rights checks, render validation.

## Phase 5 — optimization
SEO checks, publishing scheduler, analytics/retention analysis, experiments, safe community workflows, task recovery.

## Phase 6 — dashboard and hardening
Next.js dashboard, live task progress, approvals, budget controls, security/load tests, backups, observability, deployment runbooks.

A phase is complete only when code, automated tests, and verification evidence exist. Documentation/catalog entries alone do not count as working features.
