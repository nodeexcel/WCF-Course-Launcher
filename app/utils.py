import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
client = OpenAI(base_url="https://openrouter.ai/api/v1",api_key=os.getenv("OPENAI_API_KEY"))

def get_gpt_response(prompt_template: str, placeholders: dict) -> str:
    prompt = prompt_template.format(**placeholders)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}],
    )
    return response.choices[0].message.content 