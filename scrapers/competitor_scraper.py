import requests
from bs4 import BeautifulSoup


def scrape_competitor(url):

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent":
                "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = ""

        if soup.title:
            title = soup.title.text

        h1_count = len(
            soup.find_all("h1")
        )

        meta_description = ""

        meta = soup.find(
            "meta",
            attrs={
                "name":
                "description"
            }
        )

        if meta:
            meta_description = meta.get(
                "content",
                ""
            )

        return {
            "title": title,
            "meta_description":
                meta_description,
            "h1_count": h1_count
        }

    except Exception as e:

        return {
            "error": str(e)
        }