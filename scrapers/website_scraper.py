import requests
from bs4 import BeautifulSoup


def scrape_website(url):

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = soup.title.string.strip() if soup.title else ""

        meta_description = ""

        meta = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        if meta:
            meta_description = meta.get(
                "content",
                ""
            )

        h1_tags = soup.find_all("h1")

        viewport = soup.find(
            "meta",
            attrs={"name": "viewport"}
        )

        return {
            "title": title,
            "meta_description": meta_description,
            "h1_count": len(h1_tags),
            "mobile_friendly": bool(viewport)
        }

    except Exception as e:

        return {
            "error": str(e)
        }