import openai

openai.api_key = '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'

query = "how did the universe begin"

bias = ["democrat", "republican", "christian", "pastafarian"]


print(query)
for x in bias:
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": ""},
        {"role": "assistant", "content": "as a " + x},
        {"role": "user", "content": query}
    ]
    )

    print("\n\nAs a: " + x)
    print(response["choices"][0]["message"]["content"])