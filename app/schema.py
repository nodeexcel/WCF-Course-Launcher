from pydantic import BaseModel


class ChoosingNiche(BaseModel):
    target_group: str
    problem: str
    benefit: str

class MarketResearch(BaseModel):
    niche: str

class TargetGroup(BaseModel):
    niche: str

class CourseTopic(BaseModel):
    niche: str


class GenerateCourse(BaseModel):
    profession: str
    passions: str
    transformation: str
    trends: str