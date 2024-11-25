from transformers import MarianMTModel, MarianTokenizer

# Ielādējam modeli un tokenizeru latviešu uz angļu tulkošanai
model_name = "Helsinki-NLP/opus-mt-lv-en"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Latviešu valodas teikumi
latvian_texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

# Funkcija, kas tulko latviešu tekstus uz angļu valodu
def translate_to_english(texts):
    translated_texts = []
    
    for text in texts:
        # Tokenizējam ievadi
        tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        
        # Izmantojam modeli, lai tulkotu tekstu
        translated = model.generate(**tokens)
        
        # Atšifrējam ģenerēto tekstu un pievienojam rezultātu
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        translated_texts.append(translated_text)
    
    return translated_texts

# Tulkojam tekstus
translated_texts = translate_to_english(latvian_texts)

# Izvade
for i, text in enumerate(latvian_texts):
    print(f"Latviešu teikums: {text}")
    print(f"Tulkojums uz angļu valodu: {translated_texts[i]}")
    print()
