def clear_specific_words(text,word):
   text = text.split(word)
   text = " ".join(text)
   return text

print(clear_specific_words('heelo world' ,'heelo'))





