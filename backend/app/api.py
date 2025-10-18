from fastapi import APIRouter
from pydantic import BaseModel
from app.openai_client import ask_ai
from app.adapters.mock_adapter import search_mock

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    user_profile: dict | None = None

@router.post('/search')
async def search(request: QueryRequest):
    # 1) Ask AI what to clarify
    prompt = f"User asked: {request.query}. Determine if more info is needed and list slots to ask."
    ai_response = await ask_ai(prompt)

    # For MVP: if AI asks for clarification, return that question
    if 'ask:' in ai_response.lower():
        return {"action": "clarify", "message": ai_response}

    # 2) Search mock adapters
    results = search_mock(request.query)

    return {"action": "results", "items": results}
