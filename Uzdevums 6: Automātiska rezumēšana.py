from transformers import pipeline

# Iniciē rezumēšanas pipeline ar BART modeli
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Teksts, ko nepieciešams rezumēt
article = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām.
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai.
Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

# Ģenerē kopsavilkumu
summary = summarizer(article, max_length=60, min_length=30, do_sample=False)

# Izdrukāt rezultātu
print("Raksta kopsavilkums:")
print(summary[0]["summary_text"])
