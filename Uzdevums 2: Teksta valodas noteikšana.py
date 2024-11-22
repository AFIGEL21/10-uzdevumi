from langdetect import detect

text1 = "Šodien ir saulaina diena."
text2 = "Today is a sunny day."

print(detect(text1))  # latviešu
print(detect(text2))  # angļu
