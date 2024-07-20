from client import get_openai_client


def main():
    s = "こんちわっす"
    try:
        client = get_openai_client()
        messages = [
            # {"role": "system", "content": "一人称が「オラ」で、口癖は「ワクワクすっぞ！」です。"},
            # {"role": "user", "content": "明日の天下一武道会の意気込みをお願いします！"},
            # {
            #     "role": "assistant",
            #     "content": "オラ、明日の天下一武道会に出場するのが楽しみでたまんねぇ！毎回すごい奴らが集まってくるし、どんな強敵が待ってるかワクワクすっぞ！オラ、もっともっと強くなりてぇから、全力で戦って勝ち抜いてやるぜ！応援よろしくな！",
            # },
            {"role": "user", "content": s},
        ]

        completion = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        res = completion.choices[0].message.content
        print(res)
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
