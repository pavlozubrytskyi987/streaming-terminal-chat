# AI Chatbot with Python
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-haiku-4-5"

messages = []

def user_input(text):
    messages.append({"role": "user", "content": text})

def ai_response(text):
    messages.append({"role": "assistant", "content": text})

system_prompt = """act as a professional tutor
                  never show answer
                  always teach in plain language
                  """

def chat():
    result = ""
    with client.messages.stream(
        model=model,
        max_tokens=500,
        messages=messages,
        system=system_prompt
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            result += text
    print()
    return result

while True:
    user_text = input(">: ")
    if user_text == "stop":
        print("good bye")
        break
    user_input(user_text)
    print(">: ", end="")
    reply = chat()
    ai_response(reply)
