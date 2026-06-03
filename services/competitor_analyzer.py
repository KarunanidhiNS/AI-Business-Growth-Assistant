def analyze_competitor(
        business_data,
        competitor_data):

    business_score = 0
    competitor_score = 0

    if business_data.get("title"):
        business_score += 30

    if business_data.get(
            "meta_description"):
        business_score += 30

    if business_data.get(
            "h1_count", 0) > 0:
        business_score += 40

    if competitor_data.get("title"):
        competitor_score += 30

    if competitor_data.get(
            "meta_description"):
        competitor_score += 30

    if competitor_data.get(
            "h1_count", 0) > 0:
        competitor_score += 40

    comparison = ""

    if competitor_score > business_score:

        comparison = (
            "Competitor website "
            "appears stronger."
        )

    elif competitor_score < business_score:

        comparison = (
            "Business website "
            "appears stronger."
        )

    else:

        comparison = (
            "Both websites are "
            "similar."
        )

    return {
        "business_score":
            business_score,
        "competitor_score":
            competitor_score,
        "comparison":
            comparison
    }