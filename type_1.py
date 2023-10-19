# Load Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Downloading punkt sentence tokenizer
import nltk
nltk.download('punkt')


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