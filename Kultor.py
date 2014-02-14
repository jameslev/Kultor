import random

gameBegun = 0

def intro(gameState):
	
	if(gameState == 0):
		gameState = 2
		
		print "Will you play as an Agency Director or Cult Master?"
		print ' '
		chooseFaction = raw_input("C or A\n").upper()
		chooseFaction = str(chooseFaction)
		global Faction
		if(chooseFaction == "C"):
			Faction = "Cult"
			print ' '
			print 'You chose cult.'
		else:
			Faction = 'Agency'
			print ' '
			print 'You chose agency.'
			
		if(Faction=="Cult"):
			print 'What kind of cult do you lead?'
			print '1) A cult that worships Death and it\'s masters.'
			print '2) A cult that serves beings unknowable to man.'
			print '3) A cult that aims to rule the world of mortal man.'
			chooseType = raw_input("1, 2, or 3\n")
			chooseType = str(chooseType)
			if(chooseType == "1"):
				print 'Effects to be implemented'
			if(chooseType == "2"):
				print 'Effects to be implemented'
			if(chooseType == "3"):
				print 'Effects to be implemented'
		else:
			print 'What kind of Agency do you lead?'
			print '1) An agency that works in the shadows of a government.'
			print '2) An agency that is based from a secret order dating back thousands of years in ancient societies.'
			print '3) An agency that runs behind the scenes of a faceless mega corporation.'
			chooseType = raw_input("1, 2, or 3\n")
			chooseType = str(chooseType)
			if(chooseType== "1"):
				print 'Effects to be implemented'
			if(chooseType== "2"):
				print 'Effects to be implemented'
			if(chooseType== "3"):
				print 'Effects to be implemented'
				
		print ' '
		
		if(Faction == "Cult"):
			print "What is the name of your cult?"
			CultName = raw_input()
			CultName = str(CultName)
			print "Greetings dark master of " + CultName
		else:
			print "What is the name of your agency?"
			AgName = raw_input()
			AgName = str(AgName)
			print "Greetings director of " + AgName
			
		return gameState
		

while(True)	:	
	gameBegun = intro(gameBegun)
	
	