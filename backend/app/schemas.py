from pydantic import BaseModel, HttpUrl
from typing import Optional


class AnalyzeRequest(BaseModel):
    url: HttpUrl


class AnalyzeResponse(BaseModel):
    url: str
    http_status: int
    response_time_ms: int
    title: Optional[str]
    meta_description: Optional[str]
    h1_count: int
    images_missing_alt: int
    word_count: int