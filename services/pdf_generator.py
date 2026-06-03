from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import markdown
from bs4 import BeautifulSoup


def generate_pdf(
        filename,
        report_text):

    doc = SimpleDocTemplate(
        filename
    )

    styles = (
        getSampleStyleSheet()
    )

    # Convert markdown to html
    html = markdown.markdown(
        report_text,
        extensions=["tables"]
    )

    # Remove html tags and get clean text
    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    clean_text = soup.get_text(
        "\n"
    )

    content = []

    content.append(
        Paragraph(
            "Business Analysis Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    paragraphs = clean_text.split("\n")

    for para in paragraphs:

        para = para.strip()

        if para:

            content.append(
                Paragraph(
                    para,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 5)
            )

    doc.build(content)