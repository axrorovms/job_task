import os

# Gemini API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MAX_HISTORY_MESSAGES = 10
# Gemini model to use
GEMINI_MODEL = "gemini-2.5-flash"
ASSISTANT_NAME = "ShopBot"
ASSISTANT_MODEL = "gpt-4o-mini"

# App settings
APP_NAME = "Task API"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "An API for a assistant powered by Gemini."