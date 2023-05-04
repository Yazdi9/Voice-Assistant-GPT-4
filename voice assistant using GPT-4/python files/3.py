import openai

openai.api_key = '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'

query = "who discovered america"

response3 = openai.Completion.create(
  model="text-davinci-003",
  prompt=query,
  temperature=0,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

response35 = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": ""},
    {"role": "assistant", "content": ""},
    {"role": "user", "content": query}
  ]
)

print("GPT 3.0 Says:")
print(response3["choices"][0]["text"])

print("\nGPT 3.5 Turbo Says:")
print(response35["choices"][0]["message"]["content"])