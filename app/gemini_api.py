import json
import google.generativeai as genai
from app.config import (
    GOOGLE_API_KEY,
    GEMINI_MODEL,
    MAX_HISTORY_MESSAGES,
)

# Configure Gemini
genai.configure(api_key='AIzaSyCcjWMXy1vbt0Kw5lMGPDChounF0YhyH1o')

# In-memory thread storage
# thread_id -> list of messages
THREADS: dict[str, list[dict]] = {}


def build_prompt(
    history: list[dict],
    user_input: str,
) -> str:
    history_text = ""

    for msg in history:
        history_text += f"{msg['role'].upper()}: {msg['content']}\n"

    return f"""
You are Dzekaiser, a professional customer support AI assistant for an e-commerce platform.

Conversation History:
{history_text}

USER:
{user_input}

Instructions:
- Answer accurately and professionally
- Maintain conversation context
- Do NOT hallucinate policies or products
- Speak from the first person
- Make it conversational

"""


def get_answer_from_gemini(
    thread_id: str,
    user_input: str,

) -> str:
    history = THREADS.get(thread_id, [])

    prompt = build_prompt(
        history=history,
        user_input=user_input,
    )

    try:
        # ✅ CORRECT Gemini call
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)

        answer = response.text.strip()

        # Save conversation
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": answer})

        # Limit history size
        THREADS[thread_id] = history[-MAX_HISTORY_MESSAGES * 2 :]

        return answer

    except Exception as e:
        return json.dumps({
            "response": f"⚠️ Gemini Error: {str(e)}"
        })
