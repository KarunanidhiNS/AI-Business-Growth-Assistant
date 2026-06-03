from ai.prompts import (
    business_analysis_prompt
)

from ai.mistral_client import (
    ask_mistral
)


def generate_recommendations(
        business_data,
        competitor_data,
        review_data):

    prompt = business_analysis_prompt(
        business_data,
        competitor_data,
        review_data
    )

    return ask_mistral(prompt)