from bs4 import BeautifulSoup


def parse_html(html: str):

    soup = BeautifulSoup(html, "html.parser")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Title
    title = None
    if soup.title and soup.title.string:
        title = soup.title.string.strip()

    # Meta Description
    meta = soup.find("meta", attrs={"name": "description"})
    meta_description = None

    if meta:
        meta_description = meta.get("content")

    # H1 Count
    h1_count = len(soup.find_all("h1"))

    # Images without alt

    images_missing_alt = 0

    for image in soup.find_all("img"):

        alt = image.get("alt")

        if alt is None or alt.strip() == "":
            images_missing_alt += 1

    # Visible text only

    text = soup.get_text(separator=" ", strip=True)

    word_count = len(text.split())

    return {
        "title": title,
        "meta_description": meta_description,
        "h1_count": h1_count,
        "images_missing_alt": images_missing_alt,
        "word_count": word_count
    }