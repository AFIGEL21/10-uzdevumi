import re
from collections import Counter

# Teksts
text = """
Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas.
Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem.
"""

def word_frequency_analysis(text):
    # Pārvērš tekstu mazajiem burtiem un noņem interpunkciju
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    
    # Sadalīt vārdus
    words = text.split()
    
    # Skaitīt vārdu biežumu
    word_count = Counter(words)
    
    # Kopējais vārdu skaits
    total_words = len(words)
    
    return word_count, total_words

# Izsauc funkciju un iegūst rezultātus
word_count, total_words = word_frequency_analysis(text)

# Izdrukāt rezultātus
print("Vārdu biežums:")
for word, count in word_count.items():
    print(f"{word}: {count}")
    
print(f"\nKopējais vārdu skaits: {total_words}")
