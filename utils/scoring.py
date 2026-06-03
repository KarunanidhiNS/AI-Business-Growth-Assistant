def calculate_review_score(
        sentiment_report):

    total = sentiment_report["total"]

    if total == 0:
        return 50

    positive = sentiment_report["positive"]

    score = (
        positive / total
    ) * 100

    return round(score)