import spacy

# Izmanto spacy latviešu modeli (vai angļu modeli, ja latviešu modelis nav pieejams)
nlp = spacy.load("lv_core_news_sm")  # Var izmantot arī "en_core_web_sm" angļu valodai

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."
doc = nlp(text)

for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
