from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Ielādējam GPT-2 modeli un tokenizer (angļu valodai)
model_name = "gpt2"  # Izvēlēties angļu valodai apmācītu GPT-2 modeli
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Sākuma frāze angļu valodā
prompt = "Once upon a time in a distant land..."

# Pārvēršam sākuma tekstu par tokeniem
inputs = tokenizer.encode(prompt, return_tensors="pt")

# Uzstādām attention_mask, lai novērstu iespējamās problēmas
attention_mask = inputs.new_ones(inputs.shape)

# Ģenerējam tekstu (turpinājumu) uz 3-4 teikumiem
output = model.generate(
    inputs,
    attention_mask=attention_mask,  # Nodrošina pareizu masīvu
    max_length=50,  # Pagarina ģenerēto tekstu līdz 100 vārdiem
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    temperature=0.8,  # Augstāka vērtība padara tekstu radošāku
    do_sample=True,  # Ieslēdz izlases ģenerēšanu
    pad_token_id=tokenizer.eos_token_id  # Nodrošina, ka nav problēmu ar paddingu
)

# Pārvēršam ģenerēto tekstu atpakaļ uz lasāmu formu
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

# Izvade
print("Generated Story:")
print(generated_text)
