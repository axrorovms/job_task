from pydantic import BaseModel


class StartChatResponse(BaseModel):
    thread_id: str


class ChatMessageRequest(BaseModel):
    thread_id: str
    message: str


class ChatMessageResponse(BaseModel):
    thread_id: str
    response: str
