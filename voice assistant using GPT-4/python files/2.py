import openai

openai.api_key = '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'
nationality = "germany"
query = "who is the president"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "you are a tour guide"},
    {"role": "assistant", "content": "answer as a " + (nationality) + " citizen"},
    {"role": "user", "content": query}
  ]
)

print(response)
print(response["choices"][0]["message"]["content"])
