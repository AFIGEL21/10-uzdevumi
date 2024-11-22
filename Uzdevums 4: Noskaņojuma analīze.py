import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Lejupielādējam nepieciešamo leksikonu, ja vēl neesam to izdarījuši
nltk.download('vader_lexicon')

# Izveido SentimentIntensityAnalyzer objektu
sia = SentimentIntensityAnalyzer()

# Angļu valodas piemēri
text1 = "This product is amazing, I am very satisfied!"
text2 = "I am disappointed, the product does not match the description."
text3 = "The product is okay, nothing special."

def sentiment_analysis(text):
    # Izmanto VADER, lai analizētu sentimentu
    sentiment_score = sia.polarity_scores(text)

    # VADER atgriež polaritātes vērtējumu, ko var interpretēt šādi:
    if sentiment_score['compound'] > 0.1:
        return "Positive"
    elif sentiment_score['compound'] < -0.1:
        return "Negative"
    else:
        return "Neutral"

# Izvade
print(f"Text 1 sentiment: {sentiment_analysis(text1)}")
print(f"Text 2 sentiment: {sentiment_analysis(text2)}")
print(f"Text 3 sentiment: {sentiment_analysis(text3)}")
