from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Universal YouTube Agent API",
    version="0.1.0",
    description="Foundation API; integrations and autonomous workflows are under development.",
)


class SkillSummary(BaseModel):
    id: str
    group: str
    status: str


@app.get("/health", tags=["system"])
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "universal-youtube-agent"}


@app.get("/api/v1/skills", response_model=list[SkillSummary], tags=["skills"])
async def list_skills() -> list[SkillSummary]:
    from app.skills.catalog import SKILLS
    return [SkillSummary(**skill) for skill in SKILLS]
