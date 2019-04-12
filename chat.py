import aiml
Doc = aiml.Kernel()
Doc.bootstrap(learnFiles = "aiml/std-startup.xml", commands = "load aiml b")
# Doc.saveBrain("bot_brain.brn")
while True: 
	print('MediBot : ',Doc.respond(input('Human : ')))