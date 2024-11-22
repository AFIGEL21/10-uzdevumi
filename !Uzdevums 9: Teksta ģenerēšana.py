from googletrans import Translator

# Iniciē translator
translator = Translator()

text1 = "Labdien! Kā jums klājas?"
text2 = "Es šodien lasīju interesantu grāmatu."

translated_text1 = translator.translate(text1, src='lv', dest='en').text
translated_text2 = translator.translate(text2, src='lv', dest='en').text

print(translated_text1)
print(translated_text2)
