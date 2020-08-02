from nltk.corpus import wordnet
word=wordnet.synsets('sale')
#print(word)
#print(word[0].name())
print(word[0].lemmas()[0].name())
print(word[0].definition())
print(word[1].definition())
print(word[2].definition())

print(word[0].examples()[0])
print(word[0].pos())
