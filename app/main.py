from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .schema import (
    AboutMe,
    ChoosingNiche,
    ContentRollsIdeas,
    ContentRollScript,
    CourseStructure,
    CourseTopic,
    CreatingContent,
    EvergreenProduct,
    ExpertActions,
    ExpertActivities,
    GenerateCourse,
    LeadMagnetContent,
    LifeStory,
    LiveProduct,
    MarketResearch,
    MiniOffer,
    PackagingProcess,
    ProductLadder,
    SubscriptionProductStructure,
    TargetGroup)
from .prompts import (
    about_me_prompt,
    choosing_niche_prompt,
    content_rolls_ideas_prompt,
    content_roll_script_prompt,
    course_structure_prompt,
    course_topic_problem_prompt,
    creating_content_prompt,
    evergreen_product_prompt,
    expert_actions_prompt,
    expert_activities_prompt,
    generate_course_prompt,
    lead_magnet_content_prompt,
    life_story_prompt,
    live_product_prompt,
    market_research_prompt,
    mini_offer_prompt,
    packaging_process_prompt,
    product_ladder_prompt,
    subscription_product_structure_prompt,
    target_group_prompt)
from .utils import get_gpt_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=JSONResponse)
async def home():
    return JSONResponse(content={
        "message": "Welcome to the Course Creation Assistant API"}, status_code=200
    )

@app.post("/module1/choosing-niche")
async def choosing_niche(
    request: ChoosingNiche
):
    result = get_gpt_response(
        choosing_niche_prompt,
        {
            "target_group": request.target_group,
            "problem": request.problem,
            "benefit": request.benefit
        }
    )
    result_list = [line.strip() for line in result.split("\n") if line.strip()]
    return JSONResponse(content={"result": result_list}, status_code=200) 


@app.post("/module1/market-research")
async def market_research(request: MarketResearch):
    result = get_gpt_response(market_research_prompt, {"niche": request.niche})
    return JSONResponse(content={"result": result})

@app.post("/module1/target-group")
async def target_group(
    request: TargetGroup,
):
    result = get_gpt_response(
        target_group_prompt,
        {
            "niche": request.niche
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module1/course-topic")
async def course_topic(
    request: CourseTopic
):
    result = get_gpt_response(
        course_topic_problem_prompt,
        {
            "niche": request.niche
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module1/generate-course")
async def generate_course(
    request: GenerateCourse
):
    result = get_gpt_response(
        generate_course_prompt,
        {
            "profession": request.profession,
            "passions": request.passions,
            "transformation": request.transformation,
            "trends": request.trends
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module2/live-product-ideas")
async def live_product(
    request: LiveProduct
):
    result = get_gpt_response(
        live_product_prompt,
        {
            "niche": request.niche,
            "problems_list": request.problems_list,
            "target_group_description": request.target_group_description
        }
    )
    return JSONResponse(content={"result": result})


@app.post("/module2/evergreen-product-ideas")
async def evergreen_product(
    request: EvergreenProduct
):
    result = get_gpt_response(
        evergreen_product_prompt,
        {
            "niche": request.niche,
            "problems_list": request.problems_list,
            "target_group_description": request.target_group_description
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module2/product-ladder")
async def product_ladder(
    request: ProductLadder
):
    result = get_gpt_response(
        product_ladder_prompt,
        {
            "niche": request.niche,
            "problems_list": request.problems_list,
            "target_group_description": request.target_group_description
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module2/course-structure")
async def course_structure(
    request: CourseStructure
):
    result = get_gpt_response(
        course_structure_prompt,
        {
            "product_type": request.product_type,
            "product_title": request.product_title,
            "key_promise": request.key_promise,
            "niche": request.niche,
            "main_problem": request.main_problem,
            "audience": request.audience,
            "current_skills": request.current_skills,
            "target_skills": request.target_skills
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module2/subscription-product-structure")
async def subscription_product_structure(
    request: SubscriptionProductStructure
):
    result = get_gpt_response(
        subscription_product_structure_prompt,
        {
            "product_title": request.product_title,
            "key_promise": request.key_promise,
            "niche": request.niche,
            "main_problem": request.main_problem,
            "audience": request.audience,
            "current_skills": request.current_skills,
            "target_skills": request.target_skills,
            "pillar_1": request.pillar_1,
            "pillar_2": request.pillar_2,
            "pillar_3": request.pillar_3,
            "pillar_4": request.pillar_4,
            "general_topic": request.general_topic
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module2/packaging-process")
async def packaging_process(
    request: PackagingProcess
):
    result = get_gpt_response(
        packaging_process_prompt,
        {
            "course_title": request.course_title,
            "niche": request.niche,
            "main_problem": request.main_problem,
            "target_outcome": request.target_outcome,
            "num_stages": request.num_stages,
            "process_name_type": request.process_name_type
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module3/life-story")
async def life_story(
    request: LifeStory
):
    result = get_gpt_response(
        life_story_prompt,
        {
            "starting_point": request.starting_point,
            "problem": request.problem,
            "breakthrough": request.breakthrough,
            "path": request.path,
            "result": request.result,
            "key_trait": request.key_trait,
            "moral": request.moral
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module3/expert-actions")
async def expert_actions(
    request: ExpertActions
):
    result = get_gpt_response(
        expert_actions_prompt,
        {
            "niche": request.niche,
            "target_group": request.target_group,
            "problems": request.problems,
            "outcomes": request.outcomes
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module3/expert-activities")
async def expert_activities(
    request: ExpertActivities
):
    result = get_gpt_response(
        expert_activities_prompt,
        {
            "niche": request.niche,
            "experience_achievements": request.experience_achievements,
            "methodology_approach": request.methodology_approach,
            "target_group": request.target_group,
            "problems": request.problems,
            "exposure_forms": request.exposure_forms,
            "geographical_scope": request.geographical_scope,
            "languages": request.languages
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module3/creating-content")
async def creating_content(
    request: CreatingContent
):
    result = get_gpt_response(
        creating_content_prompt,
        {
            "platform": request.platform,
            "frequency": request.frequency,
            "niche": request.niche,
            "audience": request.audience,
            "formats": request.formats,
            "categories": request.categories,
            "expertise": request.expertise,
            "problems": request.problems,
            "tone": request.tone
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module4/content-rolls-ideas")
async def content_rolls_ideas(
    request: ContentRollsIdeas
):
    result = get_gpt_response(
        content_rolls_ideas_prompt,
        {
            "niche": request.niche,
            "audience": request.audience,
            "problems": request.problems,
            "topics": request.topics,
            "offer_type": request.offer_type,
            "offer_title": request.offer_title,
            "reel_types": request.reel_types,
            "tone": request.tone
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module4/content-roll-script")
async def content_roll_script(
    request: ContentRollScript
):
    result = get_gpt_response(
        content_roll_script_prompt,
        {
            "niche": request.niche,
            "offer_type": request.offer_type,
            "offer_title": request.offer_title,
            "offer_promise": request.offer_promise,
            "offer_link": request.offer_link,
            "audience": request.audience,
            "pain_point": request.pain_point,
            "goal": request.goal,
            "awareness_level": request.awareness_level,
            "reel_topic": request.reel_topic,
            "reel_tips": request.reel_tips,
            "expertise": request.expertise,
            "tone": request.tone,
            "sales_style": request.sales_style
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module4/lead-magnet-content")
async def lead_magnet_content(
    request: LeadMagnetContent
):
    result = get_gpt_response(
        lead_magnet_content_prompt,
        {
            "lead_magnet_type": request.lead_magnet_type,
            "lead_magnet_title": request.lead_magnet_title,
            "topic": request.topic,
            "promise": request.promise,
            "audience": request.audience,
            "problem": request.problem,
            "goal": request.goal,
            "awareness": request.awareness,
            "objections": request.objections,
            "topics": request.topics,
            "unique_approach": request.unique_approach,
            "benefits": request.benefits,
            "includes_tools": request.includes_tools,
            "tone": request.tone,
            "header_styles": request.header_styles
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module4/about-me")
async def about_me(
    request: AboutMe
):
    result = get_gpt_response(
        about_me_prompt,
        {
            "name_surname": request.name_surname,
            "specialization": request.specialization,
            "target_group": request.target_group,
            "help_with": request.help_with,
            "years_experience": request.years_experience,
            "main_achievements": request.main_achievements,
            "education_certifications": request.education_certifications,
            "methodology_system": request.methodology_system,
            "niche": request.niche,
            "clients_number": request.clients_number,
            "customer_results": request.customer_results,
            "awards_honors": request.awards_honors,
            "publications": request.publications,
            "speeches_lectures": request.speeches_lectures,
            "media_interviews": request.media_interviews,
            "cooperation_forms": request.cooperation_forms,
            "current_clients": request.current_clients,
            "own_projects": request.own_projects,
            "motto_philosophy": request.motto_philosophy,
            "tone": request.tone,
            "perspective": request.perspective,
            "length": request.length,
            "highlight_items": request.highlight_items
        }
    )
    return JSONResponse(content={"result": result})

@app.post("/module4/mini-offer")
async def mini_offer(
    request: MiniOffer
):
    result = get_gpt_response(
        mini_offer_prompt,
        {
            "mini_offer_type": request.mini_offer_type,
            "mini_offer_title": request.mini_offer_title,
            "niche": request.niche,
            "key_promise": request.key_promise,
            "content_format": request.content_format,
            "target_group": request.target_group,
            "pain_point": request.pain_point,
            "key_elements": request.key_elements,
            "unique_value": request.unique_value,
            "benefits": request.benefits,
            "bonuses": request.bonuses,
            "tone": request.tone,
            "sales_style": request.sales_style
        }
    )
    return JSONResponse(content={"result": result})