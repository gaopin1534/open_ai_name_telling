import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

test_jp_prompt = "TANAKAは姓ですか？名ですか？句読点を付けず姓か名で答えてください"
test_en_prompt = "is TANAKA a first name or last name? answer first or last."

response_ja = openai.Completion.create(model="text-curie-001", prompt=test_jp_prompt, temperature=0, max_tokens=7)
response_en = openai.Completion.create(model="text-curie-001", prompt=test_en_prompt, temperature=0, max_tokens=7)
print(response_ja)
print(response_en)