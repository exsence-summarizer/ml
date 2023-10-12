import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

text = "The patient has been diagnosed with Type 1 Diabetes, an autoimmune condition characterized by the body's inability to produce insulin, resulting in high blood sugar levels"

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LexRankSummarizer()
summary = summarizer(parser.document, words_count=4)



for sentence in summary:
    print(sentence)
