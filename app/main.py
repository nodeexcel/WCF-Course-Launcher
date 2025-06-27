from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .schema import (
    ChoosingNiche,
    CourseStructure,
    CourseTopic,
    EvergreenProduct,
    ExpertActions,
    GenerateCourse,
    LifeStory,
    LiveProduct,
    MarketResearch,
    PackagingProcess,
    ProductLadder,
    SubscriptionProductStructure,
    TargetGroup)
from .prompts import (
    choosing_niche_prompt,
    course_structure_prompt,
    course_topic_problem_prompt,
    evergreen_product_prompt,
    expert_actions_prompt,
    generate_course_prompt,
    life_story_prompt,
    live_product_prompt,
    market_research_prompt,
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