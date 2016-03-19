from __future__ import division  # Only if using Python 2, changes / operator to true division, not floor division  
#nltk: Natural language toolkit.  See http://www.nltk.org/
import nltk, re 
from nltk import word_tokenize

def TokenizeToSentences(filepath):
	#open file
	fh = open(filepath)
	#read file into raw unicode text
	raw = fh.read().decode('utf8')
	#tokenize into a list of sentences
	sents = nltk.sent_tokenize(raw)

	modified_sents = []
		
	#Replace \r \n characters with a space and replace multiple spaces with a single space
	for i in range(0,len(sents)):
		current_sentence = sents[i]
		current_sentence = current_sentence.replace('\n', ' ')
		current_sentence = current_sentence.replace('\r', ' ')
		current_sentence = re.sub(' +',' ', current_sentence)
		modified_sents.append(current_sentence)
			
	return modified_sents

if __name__ == "__main__":
	sents = TokenizeToSentences("./2554.txt")
	print sents[10:20]
