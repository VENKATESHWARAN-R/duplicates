import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize, sent_tokenize
#from nltk.stem import PorterStemmer
from nltk.corpus import state_union
#from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
#import random
import string






class finding_duplicate():
	def test(self, question1, question2):
		self.question1=question1
		self.question2=question2
		q1=word_tokenize(question1)
		q2=word_tokenize(question2)


		stop_words = set(stopwords.words('english'))


		filtered1=[]
		filtered2=[]

		lemmatizer=WordNetLemmatizer()

		for w in q1:
			if w not in stop_words:
				w=lemmatizer.lemmatize(w)
				filtered1.append(w)


		
		for w in q2:
			if w not in stop_words:
				w=lemmatizer.lemmatize(w)
				filtered2.append(w)

#try:
#	tagged1 = nltk.pos_tag(filtered1)
#	tagged2 = nltk.pos_tag(filtered2)

#except Exception as e:
#	print(str(e))
	

		if len(filtered1)>len(filtered2):
			big=set(filtered1)
			dig=set(filtered2)

	
		elif len(filtered1)==len(filtered2):
			big=set(filtered1)
			dig=set(filtered2)
	
		else:
			big=set(filtered2)
			dig=set(filtered1)
	
		table = str.maketrans('', '', string.punctuation)
		bigg=[w.translate(table) for w in big]
		digg=[w.translate(table) for w in dig]
		
		p=[]
		
		
		for l in range(len(bigg)):
			for j in range(len(digg)):
				k=bigg[l]
				m=digg[j]
				q=[]
				w=[]
				for syn in wordnet.synsets(k):
					for b in syn.lemmas():
						q.append(b.name())
				
				for syns in wordnet.synsets(m):
					for a in syns.lemmas():
						w.append(a.name())
				
				o=(set(q)&set(w))
				for s in range(len(o)):
					p.append(s)


		if len(p)>len(dig)/2:
			return(1)
	
		else:
			return(0)
			
			
question1=input("enter question 1: ")
question2=input("enter question 2: ")


my_classifier=finding_duplicate()


print(my_classifier.test(question1,question2))
		
		