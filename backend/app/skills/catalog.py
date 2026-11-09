"""Declarative catalog; entries are planned until implementations and tests exist."""

_GROUPS = {
    "research": ["niche_research", "competitor_intelligence", "audience_intelligence", "trend_discovery", "keyword_research"],
    "strategy": ["channel_audit", "growth_strategy", "content_calendar", "content_pillar_planning", "performance_forecasting"],
    "creative": ["video_idea_generation", "shorts_idea_generation", "script_writer", "hook_generator", "storyboard_creator"],
    "production": ["voiceover_generation", "visual_generation", "video_assembly", "caption_generation", "thumbnail_creation"],
    "publishing": ["youtube_seo", "metadata_optimizer", "publishing_scheduler", "playlist_manager", "content_quality_checker"],
    "management": ["channel_analytics", "retention_analyzer", "community_manager", "growth_optimizer", "task_recovery_manager"],
}

SKILLS = [
    {"id": skill_id, "group": group, "status": "planned"}
    for group, skill_ids in _GROUPS.items()
    for skill_id in skill_ids
]
