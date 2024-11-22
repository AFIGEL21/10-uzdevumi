import re

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

# Noņem liekos simbolus un URL
cleaned_text = re.sub(r'[@#\!\?]+', '', raw_text)
cleaned_text = re.sub(r'http\S+', '', cleaned_text)
cleaned_text = cleaned_text.lower()

print(cleaned_text)
