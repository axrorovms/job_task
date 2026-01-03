import uuid
from fastapi import FastAPI, HTTPException
from app.config import APP_NAME, APP_VERSION
from app.schemas import (
    StartChatResponse,
    ChatMessageRequest,
    ChatMessageResponse,
)
from app.gemini_api import get_answer_from_gemini, THREADS

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)


@app.post("/chat/start", response_model=StartChatResponse)
async def start_chat():
    thread_id = str(uuid.uuid4())
    THREADS[thread_id] = []
    return StartChatResponse(thread_id=thread_id)


@app.post("/chat/message", response_model=ChatMessageResponse)
async def chat_message(payload: ChatMessageRequest):
    if payload.thread_id not in THREADS:
        raise HTTPException(status_code=400, detail="Invalid thread_id")

    answer = get_answer_from_gemini(
        thread_id=payload.thread_id,
        user_input=payload.message,
    )

    return ChatMessageResponse(
        thread_id=payload.thread_id,
        response=answer,
    )
