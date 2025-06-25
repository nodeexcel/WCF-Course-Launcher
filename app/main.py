
from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse

from app.schema import *
from app.prompts import *
from app.utils import get_gpt_response

app = FastAPI()

@app.get("/", response_class=JSONResponse)
async def home():
    return JSONResponse(content={
        "message": "Welcome to the Course Creation Assistant API"}
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
    # return result_list
    print(type(result_list))
    print(len(result_list))
    print(result_list)
    return JSONResponse(content={"result": result_list}, status_code=200) 


# @app.post("/market_research")
# async def market_research(request: MarketResearch):
#     print(request.niche)
#     result = get_gpt_response(market_research_prompt, {"niche": niche})
#     return JSONResponse(content={"result": result})

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

# @app.post("/course_topic")
# async def course_topic(
#     request: Request,
#     niche: str = Form(...),
#     target_audience: str = Form(...)
# ):
#     result = get_gpt_response(
#         course_topic_problem_prompt,
#         {
#             "niche": niche,
#             "target_audience": target_audience
#         }
#     )
#     return JSONResponse(content={"result": result})

# @app.post("/generate_course")
# async def generate_course(
#     request: Request,
#     profession: str = Form(...),
#     passions: str = Form(...),
#     transformation: str = Form(...),
#     trends: str = Form(...)
# ):
#     result = get_gpt_response(
#         generate_course_prompt,
#         {
#             "profession": profession,
#             "passions": passions,
#             "transformation": transformation,
#             "trends": trends
#         }
#     )
#     return JSONResponse(content={"result": result})

# @app.post("/choosing_niche")
# async def choosing_niche(
#     request: Request,
#     target_group: str = Form(...),
#     problem: str = Form(...),
#     benefit: str = Form(...)
# ):
#     result = get_gpt_response(
#         choosing_niche_prompt,
#         {
#             "target_group": target_group,
#             "problem": problem,
#             "benefit": benefit
#         }
#     )
#     print(type(result))
#     print(len(result))
#     print(result)
#     return JSONResponse(content={"result": result}) 