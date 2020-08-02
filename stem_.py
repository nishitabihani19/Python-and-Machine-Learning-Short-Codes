'''
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
print(stemmer.stem('playing'))
'''
'''
from nltk.stem import WordNetLemmatizer
lemma=WordNetLemmatizer()
print(lemma.lemmatize('went',pos='v'))
'''
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
word=set(stopwords.words('english'))
hello='hello why sister dii loves if you a lot.'
token=word_tokenize(hello)
print(token)
#print(word)
print(len(word))
for i in token:
    if i not in word:
        print(i)
