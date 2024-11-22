from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Ielādē modelējošo valodu
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Sākuma frāze
input_text = "Reiz kādā tālā zemē"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Teksta ģenerēšana
output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)

# Ievadīt un ģenerēt tekstu
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
