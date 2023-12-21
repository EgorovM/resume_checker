from pydantic import BaseModel, Field


class ResumeRelevancy(BaseModel):
    score: float = Field(description="Score from 0 to 1, indicating how relevant the resume text is to the job vacancy.")
    strengths: list[str] = Field(description="List of strong points in the resume.")
    weaknesses: list[str] = Field(description="List of weak points in the resume that could be improved.")
    rewrite_suggestions: list[str] = Field(description="Recommendations on what could be rephrased or presented differently in the resume.")
    learning_recommendations: list[str] = Field(description="Suggestions on what skills or knowledge the applicant should acquire or improve.")
    reflection_points: list[str] = Field(description="Points for the applicant to reflect on to better understand their fit for the vacancy.")
    upgrades: str = Field(description="General tips to tailor the resume to the vacancy, in Russian.")
