from collections import Counter
import re

# Teksts, kuru analizēsim
text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

# Pārvēršam tekstu uz maziem burtiem un noņemam pieturzīmes
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)

# Izveidojam sarakstu no vārdiem
words = text.split()

# Skaitām, cik reizes katrs vārds parādās
word_counts = Counter(words)

# Izdrukājam rezultātus
for word, count in word_counts.items():
    print(f"{word}: {count}")
