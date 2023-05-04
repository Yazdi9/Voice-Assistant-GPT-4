import openai

openai.api_key = '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'

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