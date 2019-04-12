import random
import string
import json
with open('Dataset.json') as f:
	data = json.load(f)

import pandas as pd
data2 = pd.read_excel('Dataset.xlsx')
sym2=data2.columns.tolist()[1:]

cure=dict()
import aiml
Doc = aiml.Kernel()
Doc.bootstrap(learnFiles = "aiml/std-startup.xml", commands = "load aiml b")


class NLP:
	def __init__(self):
		self.disease=set()
		self.symptoms=set()
		self.sentence=''
		self.greet = True
		self.status = 1
		self.dis = data
		self.ignore_words=['are','is','am','were','i','he','she','it','you','your','yours','we','they','them','me','mine','hers','her','him','his'] 




	def verifyGreeting(self):
		for word in self.sentence.split():
			if  word.lower() in self.greeting_input:
				#self.greet = False
				return True
		return False
	


	def verifySymptoms(self):
		symlist = sym2
		tmp = set()
		flag = False
		for word in self.sentence.split():
			if word not in self.ignore_words:
				for sm in symlist:
					if word in sm.lower():
						tmp.add(sm)
						flag = True

		for i in symlist:
			if i.lower() in self.sentence:
				if i not in tmp:
					tmp.add(i)
				flag = True
		print(tmp)
		for i in tmp:
			self.symptoms.add(i)
			dise = self.findDisease(i)
			print(dise)
			if len((self.disease).intersection(dise))==0:
				self.disease = self.disease.union(dise)
			else:
				self.disease = self.disease.intersection(dise)

		return flag


	def findDisease(self,sym):
		tmp = set()
		for i in self.dis:
			if sym in self.dis[i]:
				tmp.add(i)
		return tmp



	def refresh(self):
		self.greet  = True
		self.disease = set()
		self.symptoms = set()
		self.status = 1

	def changeStatus(self,status):
		self.status=status

	def getStatus(self):
		return self.status









	def processing(self,req):
		self.sentence = req
		self.sentence  = self.sentence.lower()
		print(self.sentence)
		if 'disease' in self.sentence:
			return (1,"You may suffer from one of these diseases - "+','.join(self.disease)+'<br>')
		print(self.disease)

		k = self.verifySymptoms()
		if len(self.disease)==1:
			return (1,'You are suffering from '+','.join(self.disease)+'<br>'+'<a href ='+'cure[list(self.disease)[0]]'+'>Cure</a><br>')


		elif k:
			return (0,Doc.respond('ask more'))
		else:
			return (0,Doc.respond(self.sentence))
		
