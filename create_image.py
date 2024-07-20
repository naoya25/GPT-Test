from client import get_openai_client


def main():
    client = get_openai_client()

    res = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    print(res)
    return


if __name__ == "__main__":
    main()
