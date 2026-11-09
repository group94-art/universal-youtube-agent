# Skill catalog

These 30 entries define the intended product surface. Catalog inclusion is a specification, not proof of implementation. Each skill requires a versioned manifest, input/output schemas, permission declaration, tests, and implementation.

## Intelligence and research
1. niche_research — niche patterns, constraints, opportunity map.
2. competitor_intelligence — public competitor positioning and content patterns.
3. audience_intelligence — audience needs, questions, viewing context.
4. trend_discovery — fresh topics with source evidence.
5. keyword_research — search phrases, intent, topic clusters.

## Strategy and planning
6. channel_audit — channel baseline and gaps.
7. growth_strategy — measurable strategy and assumptions.
8. content_calendar — schedule, formats, dependencies.
9. content_pillar_planning — repeatable pillars and series.
10. performance_forecasting — scenario estimates, never guarantees.

## Creative and writing
11. video_idea_generation — long-form concepts.
12. shorts_idea_generation — short-form concepts and hooks.
13. script_writer — original scripts with source notes.
14. hook_generator — alternative openings.
15. storyboard_creator — scene-level visual/audio plan.

## Production
16. voiceover_generation — authorized synthetic or supplied voice.
17. visual_generation — visuals with provenance.
18. video_assembly — assemble assets into a timeline.
19. caption_generation — timed captions and transcript.
20. thumbnail_creation — thumbnail concept and export spec.

## Optimization and publishing
21. youtube_seo — titles, descriptions, chapters, search intent.
22. metadata_optimizer — metadata consistency and policy checks.
23. publishing_scheduler — schedule only within granted permissions.
24. playlist_manager — playlist organization with approvals as needed.
25. content_quality_checker — editorial, technical, rights, policy checks.

## Management and growth
26. channel_analytics — channel/video metric summaries.
27. retention_analyzer — retention patterns and hypotheses.
28. community_manager — response drafts and moderation recommendations.
29. growth_optimizer — evidence-based experiments.
30. task_recovery_manager — safe retry, pause, and failure reporting.

## Required manifest
Each skill declares id, version, description, input_schema, output_schema, required_permissions, allowed_tools, timeout, retry policy, idempotency behavior, data classification, retention, implementation status, and tests.

Inputs are validated; outputs are structured and traceable. Skills cannot expand their own permissions. External side effects pass through the policy engine.
