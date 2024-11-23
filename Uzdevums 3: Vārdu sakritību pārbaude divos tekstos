import re

# Teksti
text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

def calculate_word_overlap(text1, text2):
    # Funkcija, kas sagatavo vārdus: pārvērš mazajiem burtiem un noņem interpunkciju
    def preprocess_text(text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return set(text.split())
    
    # Apstrādājam abus tekstus
    words1 = preprocess_text(text1)
    words2 = preprocess_text(text2)
    
    # Atrodam kopējos vārdus
    common_words = words1 & words2
    
    # Aprēķinām sakritības līmeni procentos
    total_words = len(words1 | words2)  # Kopējais vārdu skaits
    overlap_percentage = (len(common_words) / total_words) * 100 if total_words > 0 else 0
    
    return {
        "common_words": common_words,
        "overlap_percentage": overlap_percentage
    }

# Izsauc funkciju un iegūst rezultātus
result = calculate_word_overlap(text1, text2)

# Izdrukāt rezultātus
print("Kopīgie vārdi:", result["common_words"])
print(f"Sakritības līmenis: {result['overlap_percentage']:.2f}%")
