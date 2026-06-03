def generate_business_summary(
        website_score,
        review_score,
        competitor_score):

    final_score = round(
        (
            website_score +
            review_score +
            competitor_score
        ) / 3
    )

    health = "Poor"

    if final_score >= 80:
        health = "Excellent"

    elif final_score >= 60:
        health = "Good"

    elif final_score >= 40:
        health = "Average"

    return {
        "final_score":
            final_score,
        "health":
            health
    }