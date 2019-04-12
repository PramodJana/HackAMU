import aiml
Doc = aiml.Kernel()
Doc.bootstrap(learnFiles = "aiml/std-startup.xml", commands = "load aiml b")
import json
with open('Dataset.json') as f:
	data = json.load(f)

import pandas as pd
data2 = pd.read_excel('Dataset.xlsx')
sym2=data2.columns.tolist()[1:]



cure=dict()

class Bot:
	def __init__(self):
		self.response=None
		self.sentence=None
		self.disease=set()
		self.symptoms=set()
		self.dis=data
		self.ignore_words=['are','is','am','were','i','he','she','it','you','your','yours','we','they','them','me','mine','hers','her','him','his'] 
		self.status = 1
		self.minisym=[]

	def refresh(self):
		self.disease=set()
		self.symptoms=set()

	def findDisease(self,sym):
		tmp = set()
		for i in self.dis:
			if sym in self.dis[i]:
				tmp.add(i)
		return tmp

	def verifySymptoms(self):
		symlist = sym2
		tmp = set()
		flag = False
		for word in self.sentence.split():

			if word not in self.ignore_words:
				for sm in symlist:
					if word in sm:
						tmp.add(sm)
						flag = True

		for i in symlist:
			if i in self.sentence:
				if i not in tmp:
					tmp.add(i)
				flag = True
		print(tmp)

		for i in tmp:
			self.symptoms.add(i)
			dise = self.findDisease(i)

			if len((self.disease).intersection(dise))==0:
				self.disease = self.disease.union(dise)
			else:
				self.disease = self.disease.intersection(dise)

			
		return flag






	def response(self,sentence):
		self.sentence = sentence
		self.sentence = self.sentence.lower()
		if verifySymptoms:
			if len(self.disease)==1:
				res='You are suffering from '+','.join(self.disease)+'<br>'+'<a href ='+cure[list(self.disease)[0]]+'>Cure</a><br>'
			else:
				res = Doc.respond('ask query')
		else:
			res = Doc.respond(self.sentence)

		return res

