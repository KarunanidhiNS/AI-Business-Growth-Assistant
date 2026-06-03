import sqlite3

DB_PATH = "database/business.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def insert_business(name, website, industry):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO businesses
    (business_name, website_url, industry)
    VALUES (?, ?, ?)
    """, (name, website, industry))

    conn.commit()

    business_id = cursor.lastrowid

    conn.close()

    return business_id


def save_competitor(business_id, competitor_url):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO competitors
    (business_id, competitor_url)
    VALUES (?, ?)
    """, (business_id, competitor_url))

    conn.commit()
    conn.close()


def save_report(
        business_id,
        website_score,
        competitor_score,
        final_score,
        report_data):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analysis_reports
    (
        business_id,
        website_score,
        competitor_score,
        final_score,
        report_data
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        business_id,
        website_score,
        competitor_score,
        final_score,
        report_data
    ))

    conn.commit()
    conn.close()