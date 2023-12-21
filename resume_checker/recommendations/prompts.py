from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from resume_checker.recommendations.schemas import ResumeRelevancy


resume_parser = PydanticOutputParser(pydantic_object=ResumeRelevancy)

resume_prompt = PromptTemplate(
    template="""
    Твоя задача - оценить релевантность резюме к вакансии и подсказать как улучшить вакансии под текст.
    Когда предлагаешь улучшения затронь следующие темы: сильные стороны резюме, слабые стороны резюме, 
    что стоит переписать по другому, что нужно изучить и о чем надо порефлесировать. 
    Пиши в структурированном виде, в том порядке тем, который я указал.
    Ты получишь 200$ за отличный ответ. Сделай пожалуйста задание хорошо, моя карьера зависит от твеого ответа.
    Всегда отвечай на русском языке.
    
    {format_instructions}
    
    Вакансия:
    {vacancy}"
    
    Резюме:
    {resume}"
    """,
    input_variables=["vacancy", "resume"],
    partial_variables={"format_instructions": resume_parser.get_format_instructions()},
)
