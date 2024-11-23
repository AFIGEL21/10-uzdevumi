from langdetect import detect, detect_langs

# Teksta piemēri
texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day."
]

def detect_language(texts):
    results = {}
    for text in texts:
        try:
            # Nosaka valodu
            lang = detect(text)
            # Iegūst iespējamo valodu sarakstu ar to ticamības koeficientiem
            lang_probs = detect_langs(text)
            results[text] = {"language": lang, "probabilities": lang_probs}
        except Exception as e:
            results[text] = {"error": str(e)}
    return results

# Izsauc funkciju un iegūst rezultātus
detected_languages = detect_language(texts)

# Izdrukāt rezultātus
for text, result in detected_languages.items():
    print(f"Teksts: {text}")
    if "error" in result:
        print(f"Kļūda: {result['error']}")
    else:
        print(f"Valoda: {result['language']}")
        print(f"Ticamība: {result['probabilities']}")
    print()
