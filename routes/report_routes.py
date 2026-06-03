from flask import (
    Blueprint,
    send_file,
    session
)

from services.pdf_generator import (
    generate_pdf
)

report_bp = Blueprint(
    "report",
    __name__
)


@report_bp.route("/report")
def report():
    return "Report Module Working"


@report_bp.route("/download-report")
def download_report():

    filename = (
        "reports/business_report.pdf"
    )

    report_text = session.get(
        "latest_report",
        "No Report Available"
    )

    generate_pdf(
        filename,
        report_text
    )

    return send_file(
        filename,
        as_attachment=True
    )