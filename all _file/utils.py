from nltk.stem.porter import PorterStemmer
import numpy as np
import nltk
nltk.download('punkt')

def tokenize(sentence):
  return nltk.word_tokenize(sentence)

stemmer = PorterStemmer()

def stem(word):
  return stemmer.stem(word.lower())


def bag_of_word(tokenize_sentence, all_word):
  tokenize_sentence = [stem(w) for w in tokenize_sentence]

  bag = np.zeros(len(all_word), dtype=np.float32)
  for idx, w in enumerate(all_word):
    if w in tokenize_sentence: #check for common word this is kind a like OHE
      bag[idx] = 1.0
  return bag