import asyncio
from utils import chat_with_viola
from loader import openai, whisper

# Set your OpenAI API key
openai.api_key = "sk-306d16c8c04a42c2ad0e01c7b7ee7905"  # Or use your environment variable
openai.api_base = "https://api.deepseek.com/v1"
RECORD_SECONDS = 6
FILENAME = "input.wav"
MODEL = whisper.load_model("base")  # Puoi usare "small", "medium", etc...

if __name__ == "__main__":
    asyncio.run(chat_with_viola(FILENAME, RECORD_SECONDS, MODEL))