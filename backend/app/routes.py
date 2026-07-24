from fastapi import APIRouter, HTTPException
from app.utils import calculate_seo_score
from app.schemas import AnalyzeRequest
from app.services import fetch_page
from app.parser import parse_html

router = APIRouter()


@router.post("/api/analyze")
def analyze(request: AnalyzeRequest):

    try:

        page = fetch_page(str(request.url))

        if page["status"] >= 400:

            raise HTTPException(
                status_code=page["status"],
                detail=f"Website returned HTTP {page['status']}"
            )

        if "text/html" not in page["content_type"]:

            raise HTTPException(
                status_code=400,
                detail="URL is not an HTML webpage."
            )

        parsed = parse_html(page["html"])
        seo_score, recommendations = calculate_seo_score(
    parsed,
    page["response_time"]
)
        return {
    "success": True,
    "data": {
        "url": str(request.url),
        "http_status": page["status"],
        "response_time_ms": page["response_time"],

        **parsed,

        "seo_score": seo_score,
        "recommendations": recommendations,
    }
}

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )