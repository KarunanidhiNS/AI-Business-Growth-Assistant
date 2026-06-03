import sqlite3

DB_PATH = "business.db"


def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS businesses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        business_name TEXT,
        website_url TEXT,
        industry TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS competitors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        business_id INTEGER,
        competitor_url TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis_reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        business_id INTEGER,
        website_score INTEGER,
        competitor_score INTEGER,
        final_score INTEGER,
        report_data TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database initialized successfully.")