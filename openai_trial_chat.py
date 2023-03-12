import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

test_jp_prompt = "IINUMAは姓ですか？名ですか？句読点を付けず姓か名、一単語で答えてください"
test_en_prompt = "Is Japanese name IINUMA a first name or a last name? Answer only 'first', 'last' or 'do not know'"

response_ja = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": test_jp_prompt},
    ]
)

response_en = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": test_en_prompt},
    ]
)

print(response_ja)
print(response_en)