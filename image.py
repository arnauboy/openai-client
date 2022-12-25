import openai
import webbrowser
from api_keys import API_KEY

openai.api_key = API_KEY()

request = input("Enter what you want to create:\n")

response = openai.Image.create(
  prompt=request,
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']

webbrowser.open(url = image_url, new=0)