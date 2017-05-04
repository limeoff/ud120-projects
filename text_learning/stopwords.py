from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")
print stemmer.stem("responsiveness")
print stemmer.stem("responsivity")
#sw = stopwords.words("english")

#print sw