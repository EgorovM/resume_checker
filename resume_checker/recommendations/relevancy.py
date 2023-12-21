from openai import OpenAI

from resume_checker.recommendations.prompts import resume_prompt, resume_parser
from resume_checker.recommendations.schemas import ResumeRelevancy
from resume_checker.settings import OPENAI_API_KEY

client = OpenAI(
    # This is the default and can be omitted
    api_key=OPENAI_API_KEY,
)


def get_score_and_edits(vacancy_text: str, resume_text: str) -> dict:
    prompt = resume_prompt.format_prompt(vacancy=vacancy_text, resume=resume_text)

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": prompt.to_string()},
            {"role": "user", "content": "Оцени предоставлееное резюме пожалуйста"}
        ],
        temperature=0,
        response_format={"type": "json_object"}
    )

    output = response.choices[0].message.content.strip()

    result: ResumeRelevancy = resume_parser.parse(output)

    return dict(result)

