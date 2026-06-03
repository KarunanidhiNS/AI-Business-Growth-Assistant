def calculate_website_score(data):

    score = 0

    if data.get("title"):
        score += 25

    if data.get("meta_description"):
        score += 25

    if data.get("h1_count", 0) > 0:
        score += 25

    if data.get("mobile_friendly"):
        score += 25

    return {
        "website_score": score
    }