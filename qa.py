import openai
from api_keys import API_KEY

openai.api_key = API_KEY()

request = input("Enter what you want to say to ChatGPT:\n")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=request,
  max_tokens=100,
)

print(response.choices[0].text)