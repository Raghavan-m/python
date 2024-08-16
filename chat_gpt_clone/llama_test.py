
from dotenv import load_dotenv

load_dotenv()

from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": "hello\n"
        }
    ],
    temperature=1,
    max_tokens=8192,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
