import re

# Neapstrādāts teksts
raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

def clean_and_normalize_text(text):
    # 1. Noņem @pieminējumus
    text = re.sub(r'@\w+', '', text)
    
    # 2. Noņem URL
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # 3. Noņem emocijzīmes un citus simbolus
    text = re.sub(r'[^\w\s]', '', text, flags=re.UNICODE)
    
    # 4. Noņem liekās atstarpes
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 5. Pārveido uz mazajiem burtiem
    text = text.lower()
    
    return text

# Izsauc funkciju un iegūst tīro tekstu
cleaned_text = clean_and_normalize_text(raw_text)

# Izdrukāt rezultātu
print("Tīrs teksts:")
print(cleaned_text)
