from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .schema import (
    ChoosingNiche,
    CourseTopic,
    GenerateCourse,
    MarketResearch,
    TargetGroup)
from .prompts import (
    choosing_niche_prompt,
    course_topic_problem_prompt,
    generate_course_prompt,
    market_research_prompt,
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
