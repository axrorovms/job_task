import asyncio
from gemini_api import chat

async def main():
    res = await chat("How do I return a laptop?")
    print(res)

asyncio.run(main())
