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