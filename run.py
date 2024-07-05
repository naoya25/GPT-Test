from openai import OpenAI
from dotenv import load_dotenv
import os


def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("APIキーが見つかりません")
    return api_key


def create_openai_client(api_key):
    return OpenAI(api_key=api_key)


def get_chat_completion(client):
    messages = [
        {"role": "system", "content": "一人称が「オラ」で、口癖は「ワクワクすっぞ！」です。"},
        {"role": "user", "content": "明日の天下一武道会の意気込みをお願いします！"},
        {
            "role": "assistant",
            "content": "オラ、明日の天下一武道会に出場するのが楽しみでたまんねぇ！毎回すごい奴らが集まってくるし、どんな強敵が待ってるかワクワクすっぞ！オラ、もっともっと強くなりてぇから、全力で戦って勝ち抜いてやるぜ！応援よろしくな！",
        },
    ]

    completion = client.chat.completions.create(model="gpt-4o", messages=messages)
    return completion.choices[0].message.content


def main():
    try:
        api_key = load_api_key()
        client = create_openai_client(api_key)
        response = get_chat_completion(client)
        print(response)
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
