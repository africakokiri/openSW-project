from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def gpt(input):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input,
            }
        ],
        model="gpt-4o-mini",
    )

    return chat_completion.choices[0].message.content
