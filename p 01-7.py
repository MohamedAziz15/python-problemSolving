def redundancyWord(text,word):
   counter =0
   for i in text.split(' '):
       if i == word:
           counter +=1
   return counter

print(redundancyWord('heelo world world world' ,'world'))


