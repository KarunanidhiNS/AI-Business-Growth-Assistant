from textblob import TextBlob


def analyze_reviews(reviews):

    positive = 0
    negative = 0
    neutral = 0

    complaints = {}

    complaint_keywords = [
        "slow",
        "delay",
        "late",
        "expensive",
        "poor",
        "bad",
        "issue",
        "problem",
        "support",
        "service"
    ]

    for review in reviews:

        sentiment = (
            TextBlob(review)
            .sentiment
            .polarity
        )

        if sentiment > 0:
            positive += 1

        elif sentiment < 0:
            negative += 1

        else:
            neutral += 1

        review_lower = review.lower()

        for keyword in complaint_keywords:

            if keyword in review_lower:

                complaints[keyword] = (
                    complaints.get(keyword, 0) + 1
                )

    total = len(reviews)

    sentiment_report = {
        "positive":
            positive,
        "negative":
            negative,
        "neutral":
            neutral,
        "total":
            total
    }

    sorted_complaints = sorted(
        complaints.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return {
        "sentiment_report":
            sentiment_report,
        "complaints":
            sorted_complaints[:5]
    }