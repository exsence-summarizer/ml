# Load Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


def summarize_text(text, n):
    
    # Creating text parser using tokenization
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    # Summarize using sumy TextRank
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, n)

    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    return text_summary


text = """
The patient has been diagnosed with Type 1 Diabetes, an autoimmune condition characterized by the body's inability to produce insulin, resulting in high blood sugar levels
"""


print(summarize_text(text, 1))