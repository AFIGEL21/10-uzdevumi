import re
from collections import Counter

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

# Tīra tekstu no liekajiem simboliem un pārvērš to par maziem burtiem
text = text.lower()
words = re.findall(r'\w+', text)

# Skaita katra vārda biežumu
word_counts = Counter(words)

# Izvade
for word, count in word_counts.items():
    print(f"{word}: {count}")
