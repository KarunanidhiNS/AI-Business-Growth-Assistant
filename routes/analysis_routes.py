import os
import markdown
from flask import session
from scrapers.review_scraper import (
    load_reviews
)

from services.review_analyzer import (
    analyze_reviews
)

from flask import (
    Blueprint,
    request,
    render_template
)

from utils.scoring import (
    calculate_review_score
)

from services.priority_engine import (
    calculate_priority
)

from services.report_generator import (
    generate_business_summary
)

from database.db_operations import (
    insert_business
)

from scrapers.website_scraper import (
    scrape_website
)

from scrapers.competitor_scraper import (
    scrape_competitor
)

from services.website_analyzer import (
    calculate_website_score
)

from services.competitor_analyzer import (
    analyze_competitor
)

from ai.recommendation_engine import (
    generate_recommendations
)

analysis_bp = Blueprint(
    "analysis",
    __name__
)


@analysis_bp.route(
    "/analyze-business",
    methods=["POST"]
)
def analyze_business():

    business_name = request.form.get(
        "business_name"
    )

    website_url = request.form.get(
        "website_url"
    )

    industry = request.form.get(
        "industry"
    )

    competitor1 = request.form.get(
        "competitor1"
    )

    insert_business(
        business_name,
        website_url,
        industry
    )

    # website_data = scrape_website(
    #     website_url
    # )

    # website_score = (
    #     calculate_website_score(
    #         website_data
    #     )
    # )

    website_data = scrape_website(
        website_url
    )

    if "error" in website_data:

        return render_template(
            "error.html",
            error_message=website_data["error"]
        )

    website_score = (
        calculate_website_score(
            website_data
        )
    )

    competitor_data = {}
    comparison_result = {}
    competitor_score = 50

    if competitor1:

        competitor_data = (
            scrape_competitor(
                competitor1
            )
        )

        comparison_result = (
            analyze_competitor(
                website_data,
                competitor_data
            )
        )

        competitor_score = (
            comparison_result.get(
                "competitor_score",
                50
            )
        )

    review_analysis = {}
    review_score = 50
    reviews = []

    uploaded_file = request.files.get(
        "reviews_file"
    )

    print("FILES:", request.files)
    print("UPLOADED FILE:", uploaded_file)

    if uploaded_file:

        save_path = os.path.join(
            "static/uploads/reviews",
            uploaded_file.filename
        )

        uploaded_file.save(
            save_path
        )

        # reviews = load_reviews(
        #     save_path
        # )
        # print("Reviews Loaded:", reviews)

        # review_analysis = (
        #     analyze_reviews(
        #         reviews
        #     )
        # )
        reviews = load_reviews(save_path)

        print("Reviews from CSV:", reviews)

        review_analysis = analyze_reviews(reviews)

        print("Review Analysis:", review_analysis)

        # reviews = [
        #     "Excellent software development service.",
        #     "Support response is slow.",
        #     "Very professional developers.",
        #     "Project delivery was delayed."
        # ]

        # review_analysis = analyze_reviews(reviews)

        print(review_analysis)

        review_score = (
            calculate_review_score(
                review_analysis[
                    "sentiment_report"
                ]
            )
        )
        print("Review Analysis:", review_analysis)

    # ai_report = (
    #     generate_recommendations(
    #         website_data,
    #         competitor_data,
    #         review_analysis
    #     )
    # )
    ai_report = generate_recommendations(
        website_data,
        competitor_data,
        review_analysis
    )
    session["latest_report"] = ai_report

    ai_report_html = markdown.markdown(
        ai_report,
        extensions=["tables"]
    )

    summary = (
        generate_business_summary(
            website_score[
                "website_score"
            ],
            review_score,
            competitor_score
        )
    )

    priorities = (
        calculate_priority(
            website_score[
                "website_score"
            ],
            competitor_score,
            review_score
        )
    )

    return render_template(
        "analysis.html",
        business_name=business_name,
        website_data=website_data,
        website_score=website_score,
        competitor_data=competitor_data,
        comparison=comparison_result,
        review_analysis=review_analysis,
        # ai_report=ai_report,
        ai_report=ai_report_html,
        summary=summary,
        priorities=priorities,
        review_score=review_score,
        competitor_score=competitor_score
    )