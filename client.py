from openai import OpenAI
from dotenv import load_dotenv
import os


def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("APIキーが見つかりません")
    return api_key


def get_openai_client():
    api_key = load_api_key()
    return OpenAI(api_key=api_key)
