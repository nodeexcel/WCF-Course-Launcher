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
    
class LiveProduct(BaseModel):
    niche: str
    problems_list: str
    target_group_description: str
    
class EvergreenProduct(BaseModel):
    niche: str
    problems_list: str
    target_group_description: str
    
class ProductLadder(BaseModel):
    niche: str
    problems_list: str
    target_group_description: str
    
class CourseStructure(BaseModel):
    product_type: str
    product_title: str
    key_promise: str
    niche: str
    main_problem: str
    audience: str
    current_skills: str
    target_skills: str
    
class SubscriptionProductStructure(BaseModel):
    product_title: str
    key_promise: str
    niche: str
    main_problem: str
    audience: str
    current_skills: str
    target_skills: str
    pillar_1: str
    pillar_2: str
    pillar_3: str
    pillar_4: str
    general_topic: str
    
class PackagingProcess(BaseModel):
    course_title: str
    niche: str
    main_problem: str
    target_outcome: str
    num_stages: str
    process_name_type: str
    
class LifeStory(BaseModel):
    starting_point: str
    problem: str
    breakthrough: str
    path: str
    result: str
    key_trait: str
    moral: str
    
class ExpertActions(BaseModel):
    niche: str
    target_group: str
    problems: str
    outcomes: str