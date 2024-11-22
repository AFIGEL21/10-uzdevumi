from textblob import TextBlob

# Angļu valodas piemēri
text1 = "This product is amazing, I am very satisfied!"
text2 = "I am disappointed, the product does not match the description."
text3 = "The product is okay, nothing special."

def sentiment_analysis(text):
    # Izveido TextBlob objektu
    blob = TextBlob(text)
    
    # Iegūst polaritāti (kā noskaņojums)
    polarity = blob.sentiment.polarity
    
    # Nosaka noskaņojumu
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Izvade
print(f"Text 1 sentiment: {sentiment_analysis(text1)}")
print(f"Text 2 sentiment: {sentiment_analysis(text2)}")
print(f"Text 3 sentiment: {sentiment_analysis(text3)}")
