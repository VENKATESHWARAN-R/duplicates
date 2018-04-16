import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import state_union
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string






class finding_duplicate():
		
	def test(self, question1, question2):
		self.question1=question1.lower()
		self.question2=question2.lower()
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
		
		s=[]
		a=[]
		
		
		
		for l in range(len(bigg)):
			for j in range(len(digg)):
				k=bigg[l]
				m=digg[j]
				syn1=[]
				syn2=[]
				ant1=[]
				ant2=[]
				for syn in wordnet.synsets(k):
					for b in syn.lemmas():
						syn1.append(b.name())
						if b.antonyms():
							ant1.append(b.antonyms()[0].name())
				
				for syns in wordnet.synsets(m):
					for v in syns.lemmas():
						syn2.append(v.name())
						if v.antonyms():
							ant2.append(v.antonyms()[0].name())
				
				o=(set(syn1)&set(syn2))
				q=(set(ant1)&set(ant2))
				for n in range(len(o)):
					s.append(n)
					
				for t in range(len(q)):
					a.append(t)


		if len(s)>len(dig)/2:
			if len(a)==0:
				print(1)
			
			else:
				print(0)
	
		else:
			print(0)
			
			
		
	
			
			
question1=input("enter question 1: ")
question2=input("enter question 2: ")


my_classifier=finding_duplicate()


my_classifier.test(question1,question2)
		
		