# Universal YouTube Agent

A niche-agnostic, modular agent platform for planning, producing, optimizing, scheduling, and learning from YouTube content workflows.

**Status: foundation in progress.** This repository is not yet a production-ready autonomous publisher. Features are marked implemented only after code and tests exist.

## Goals
- Support multiple channels and all content niches.
- Orchestrate specialized skills with validated contracts.
- Research audiences, competitors, trends, and search intent.
- Create content plans, scripts, storyboards, metadata, and production briefs.
- Build media pipelines using replaceable providers and FFmpeg.
- Analyze performance and improve plans using evidence.
- Keep channel memory, assets, tasks, and approvals isolated.

## Stack
Python 3.12+, FastAPI, Pydantic; planned Next.js/TypeScript frontend; PostgreSQL/Supabase-compatible persistence; Redis workers; YouTube Data and Analytics APIs; FFmpeg; S3-compatible storage.

## Quick start
From `backend/`:
```bash
python -m venv .venv
# activate the environment, then:
pip install -e ".[dev]"
uvicorn app.main:app --reload
```
Check `/health`, `/api/v1/skills`, and `/docs`.

## Docs
- [Architecture](docs/ARCHITECTURE.md)
- [30-skill catalog](docs/SKILLS.md)
- [Security](docs/SECURITY.md)
- [Roadmap](docs/ROADMAP.md)

## Credentials
Never commit real API keys, OAuth secrets, refresh tokens, service-role keys, or passwords. Use local environment variables or a secret manager. Publishing and spending remain permission-gated.

A skill in the catalog is a specification until its implementation and tests are present. Public repository visibility does not grant a license; no license has been selected yet.
