import openai

openai.api_key = 'Your_API_KEY'

query = "what was the battle of the frank"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=query,
  temperature=0,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

print(response)

print(response["choices"][0]["text"])
