import spacy

# Ielādējam universālo modeli ar NER spējām
nlp = spacy.load("xx_ent_wiki_sm")

# Ievades teksts
text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

# Pārveidojam tekstu uz nlp objektu
doc = nlp(text)

# Funkcija, lai identificētu un izvadītu īpašas vienības
def extract_named_entities(doc):
    person_names = []
    organizations = []
    
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            person_names.append(ent.text)
        elif ent.label_ == "ORG":
            organizations.append(ent.text)
    
    return person_names, organizations

# Iegūstam un izdrukājam rezultātus
person_names, organizations = extract_named_entities(doc)

print("Personvārdi:", person_names)
print("Organizācijas:", organizations)
