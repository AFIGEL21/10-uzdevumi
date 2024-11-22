from langdetect import detect

# Funkcija valodas noteikšanai
def detect_language(text):
    try:
        language = detect(text)  # Izmanto langdetect funkciju valodas noteikšanai
        return language
    except Exception as e:
        return f"Error: {str(e)}"  # Ja notiek kļūda, atgriežam kļūdas ziņojumu

while True:
    # Lietotājs ievada tekstu
    text = input("Lūdzu, ievadiet tekstu (vai ierakstiet 'beigt', lai izietu): ")

    # Ja lietotājs ievada 'beigt', programma beigsies
    if text.lower() == 'beigt':
        print("Programma beidz darbību.")
        break

    # Noteikt valodu
    language = detect_language(text)

    # Izvadīt rezultātu
    print(f"Teksts ir uzrakstīts šādā valodā: {language}")
