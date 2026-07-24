import time
import httpx


def fetch_page(url: str):
    """
    Fetch webpage and return
    HTML,
    HTTP Status,
    Response Time,
    Content-Type
    """

    try:
        start = time.perf_counter()

        response = httpx.get(
            url,
            timeout=10,
            follow_redirects=True,
            headers={
                "User-Agent": "PagePulse/1.0"
            }
        )

        end = time.perf_counter()

        return {
            "html": response.text,
            "status": response.status_code,
            "response_time": round((end - start) * 1000),
            "content_type": response.headers.get("content-type", "")
        }

    except httpx.TimeoutException:
        raise Exception("Request timed out.")

    except httpx.ConnectError:
        raise Exception("Could not connect to website.")

    except httpx.RequestError:
        raise Exception("Network request failed.")