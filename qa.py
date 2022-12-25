import os
import openai
from api_keys import API_KEY

openai.api_key = API_KEY()

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=100,
)

print(response)