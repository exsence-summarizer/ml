import nltk

nltk.download('punkt')



text = "The patient has been diagnosed with Type 1 Diabetes, an autoimmune condition characterized by the body's inability to produce insulin, resulting in high blood sugar levels"


def summarize_to_words(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    summarized_words = " ".join(words[:4])
    return summarized_words

summary = summarize_to_words(text)
print(summary)


curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}]
  }'
