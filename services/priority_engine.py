def calculate_priority(
        website_score,
        competitor_score,
        review_score):

    priorities = []

    if website_score < 70:

        priorities.append({
            "action":
            "Improve Website SEO and Structure",
            "priority":
            "HIGH"
        })

    if competitor_score > website_score:

        priorities.append({
            "action":
            "Close Competitor Feature Gap",
            "priority":
            "HIGH"
        })

    if review_score < 70:

        priorities.append({
            "action":
            "Improve Customer Satisfaction",
            "priority":
            "HIGH"
        })

    if not priorities:

        priorities.append({
            "action":
            "Maintain Current Growth Strategy",
            "priority":
            "LOW"
        })

    return priorities