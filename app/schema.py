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
    
class ExpertActivities(BaseModel):
    niche: str
    experience_achievements: str
    methodology_approach: str
    target_group: str
    problems: str
    exposure_forms: str
    geographical_scope: str
    languages: str
    
class CreatingContent(BaseModel):
    platform: str
    frequency: str
    niche: str
    audience: str
    formats: str
    categories: str
    expertise: str
    problems: str
    tone: str
    
class ContentRollsIdeas(BaseModel):
    niche: str
    audience: str
    problems: str
    topics: str
    offer_type: str
    offer_title: str
    reel_types: str
    tone: str
    
class ContentRollScript(BaseModel):
    niche: str
    offer_type: str
    offer_title: str
    offer_promise: str
    offer_link: str
    audience: str
    pain_point: str
    goal: str
    awareness_level: str
    reel_topic: str
    reel_tips: str
    expertise: str
    tone: str
    sales_style: str
    
class LeadMagnetContent(BaseModel):
    lead_magnet_type: str
    lead_magnet_title: str
    topic: str
    promise: str
    audience: str
    problem: str
    goal: str
    awareness: str
    objections: str
    topics: str
    unique_approach: str
    benefits: str
    includes_tools: str
    tone: str
    header_styles: str
    
class AboutMe(BaseModel):
    name_surname: str
    specialization: str
    target_group: str
    help_with: str
    years_experience: str
    main_achievements: str
    education_certifications: str
    methodology_system: str
    niche: str
    clients_number: str
    customer_results: str
    awards_honors: str
    publications: str
    speeches_lectures: str
    media_interviews: str
    cooperation_forms: str
    current_clients: str
    own_projects: str
    motto_philosophy: str
    tone: str
    perspective: str
    length: str
    highlight_items: str
    
class MiniOffer(BaseModel):
    mini_offer_type: str
    mini_offer_title: str
    niche: str
    key_promise: str
    content_format: str
    target_group: str
    pain_point: str
    key_elements: str
    unique_value: str
    benefits: str
    bonuses: str
    tone: str
    sales_style: str