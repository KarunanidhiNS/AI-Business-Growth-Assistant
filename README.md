# AI Business Growth Assistant

## Overview

AI Business Growth Assistant is an AI-powered business intelligence platform that helps local businesses identify growth opportunities, customer pain points, competitor advantages, and actionable recommendations.

The system analyzes a business website, customer reviews, and competitor websites to generate evidence-based insights and a prioritized action plan for business growth.

---

## Problem Statement

Many local businesses experience slow growth but often struggle to identify the root causes.

This project helps business owners answer:

* What problems are affecting business growth?
* What opportunities exist?
* What evidence supports these findings?
* What actions should be taken?
* Which actions should be prioritized first?

---

## Features

### Website Analysis

* Website scraping and content extraction
* Meta title analysis
* Meta description analysis
* Heading structure analysis
* Website quality assessment

### Customer Review Analysis

* CSV review upload
* Sentiment analysis
* Positive review detection
* Negative review detection
* Complaint keyword detection
* Customer satisfaction scoring

### Competitor Analysis

* Competitor website analysis
* Feature comparison
* Competitive benchmarking
* Strength and weakness identification

### AI-Powered Insights

* Business health assessment
* Opportunity detection
* Problem identification
* Growth recommendations
* Strategic action plans

### Reporting

* Business analysis summary
* Key findings
* Competitor insights
* Recommendations
* Prioritized action plan
* PDF report export

---

## System Workflow

1. User enters business details.
2. User provides website URL.
3. User uploads customer reviews (CSV).
4. User provides competitor website URLs.
5. Website data is scraped and analyzed.
6. Customer reviews are processed using sentiment analysis.
7. Competitor websites are analyzed.
8. AI generates business insights and recommendations.
9. Priority engine ranks recommended actions.
10. Business report is generated and exported as PDF.

---

## Tech Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Backend

* Python
* Flask
* Jinja2

### Database

* SQLite

### AI & NLP

* Mistral AI API
* TextBlob

### Data Processing

* Pandas

### Web Scraping

* Requests
* BeautifulSoup4

### PDF Generation

* ReportLab

---

## Project Structure

```text
AI-Business-Growth-Assistant/

├── app.py
├── config.py
├── requirements.txt

├── database/
├── routes/
├── services/
├── scrapers/
├── models/
├── utils/
├── ai/

├── templates/
├── static/

├── reports/
├── datasets/
```

## Installation

### Clone Repository

```bash
git clone https://github.com/KarunanidhiNS/AI-Business-Growth-Assistant.git

cd AI-Business-Growth-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

MISTRAL_API_KEY=your_mistral_api_key
```

---

## Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Sample Review CSV Format

```csv
review
Excellent software development service.
Support response is slow.
Very professional developers.
Project delivery was delayed.
```

---

## Generated Outputs

The system generates:

* Business Health Score
* Website Analysis
* Customer Review Insights
* Competitor Analysis
* Key Findings
* Growth Opportunities
* Recommendations
* Priority Action Plan
* PDF Report

---

## Screenshots

(screenshots/01.png)

![Website Analysis](screenshots/website-analysis.png)

![Customer Review Analysis](screenshots/review-analysis.png)

![Competitor Analysis](screenshots/competitor-analysis.png)

![AI Insights](screenshots/ai-insights.png)

![Action Plan](screenshots/action-plan.png)

![PDF Report](screenshots/pdf-report.png)


## Future Enhancements

* Google Reviews API Integration
* Multi-Competitor Comparison
* Interactive Analytics Dashboard
* Advanced SEO Analysis
* AI Chat Assistant
* Business Trend Prediction
* Email Report Delivery

---

## Author

Karunanidhi N S

Python Developer | Full Stack Developer | AI Developer

---

