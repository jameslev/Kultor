import sys
import random
import os

gameBegun = 0

gameOn = True

class Orgi:
	
	def __init__(self, type, name, obscurity, trials, supsci, occult, influence, unknown):
		self.type=type
		self.name=name
		self.ob = obscurity
		self.trials = trials
		self.supsci = supsci
		self.occult = occult
		self.influ = influence
		self.unknown = unknown
		
		
class Cultist:
	stealth = 0
	cweps = 0
	occult = 0
	supsci = 0
	persu = 0
	loyalty = 0
	
	slot1 = None
	slot2 = None
	slot3 = None
	
	def __init__(self, name, trial, occult, obscurity, supsci, influence):
		self.name = name
		self.trial = trial
		Cultist.stealth = random.randint(0,trial)
		Cultist.cweps = random.randint(0,trial)
		Cultist.occult = random.randint(0,trial)
		Cultist.supsci = random.randint(0,trial)
		Cultist.persu = random.randint(0,trial)
		Cultist.loyalty = random.randint(0,trial)
		if(occult==4 or occult==8):
			Cultist.occult+=occult/4
		if(obscurity==4 or obscurity==8):
			Cultist.stealth+=obscurity/4
		if(supsci==4 or supsci==8):
			Cultist.supsci+=supsci/4
		if(influence==4 or influence==8):
			Cultist.persu+=persu/4
		#Cultist.slot1 = None
		#Cultist.slot2 = None
		#Cultist.slot3 = None
		
	def caplock(self):
		if(Cultist.stealth>10):
			Cultist.stealth==10
		if(Cultist.cweps>10):
			Cultist.cweps==10
		if(Cultist.occult>10):
			Cultist.occult==10
		if(Cultist.supsci>10):
			Cultist.supsci==10
		if(Cultist.persu>10):
			Cultist.persu==10
		if(Cultist.loyalty>10):
			Cultist.loyalty==10
			
	def inventory(self, item, remove):
		if(Cultist.slot1 is not None and Cultist.slot2 is not None and Cultist.slot3 is not None):
			print 'Inventory full'
			
		if(Cultist.slot3 is None and Cultist.slot1 is not None and Cultist.slot2 is not None):
			Cultist.slot3=item
			print item +'stored in slot 3'
		if(Cultist.slot2 is None and Cultist.slot1 is not None):
			Cultist.slot2=item
			print item +'stored in slot 2'
		if(Cultist.slot1 is None):
			Cultist.slot1=item
			print item+'stored in slot 1'
		
		if(remove==Cultist.slot1):
			Cultist.slot1 = None
		if(remove==Cultist.slot2):
			Cultist.slot2 = None
		if(remove==Cultist.slot3):
			Cultist.slot3 = None

def loadnames():
	rawfile = open("names.txt","r")
	
	
	allnames = rawfile.read()
	
	splitnames = allnames.splitlines()

	rawfile.close()
	
	return splitnames

def intro():
		
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
		
def initvalues():
	if(Faction=="Cult"):
		print 'What kind of cult do you lead?'
		print '1) A cult that worships Death and it\'s masters.'
		print '2) A cult that serves beings unknowable to man.'
		print '3) A cult that aims to rule the world of mortal man.'
		chooseType = raw_input("1, 2, or 3\n")
		chooseType = str(chooseType)
		if(chooseType == "1"):
			print 'Effects to be implemented'
			initchoice = 1
		if(chooseType == "2"):
			print 'Effects to be implemented'
			initchoice = 2
		if(chooseType == "3"):
			print 'Effects to be implemented'
			initchoice = 3
	else:
		print 'What kind of Agency do you lead?'
		print '1) An agency that works in the shadows of a government.'
		print '2) An agency that is based from a secret order dating back thousands of years in ancient societies.'
		print '3) An agency that runs behind the scenes of a faceless mega corporation.'
		chooseType = raw_input("1, 2, or 3\n")
		chooseType = str(chooseType)
		if(chooseType== "1"):
			print 'Effects to be implemented'
			initchoice = 4
		if(chooseType== "2"):
			print 'Effects to be implemented'
			initchoice = 5
		if(chooseType== "3"):
			print 'Effects to be implemented'
			initchoice = 6
			
	print ' '
	return initchoice
			
def nameIt():
	if(Faction == "Cult"):
		print "What is the name of your cult?"
		CultName = raw_input()
		CultName = str(CultName)
		print "Greetings dark master of " + CultName
		
		return CultName
		
	else:
		print "What is the name of your agency?"
		AgName = raw_input()
		AgName = str(AgName)
		print "Greetings director of " + AgName
		
		return AgName

def endSetup():
	gameBegun=1
	return gameBegun

def events():
	print 'Stuff happend last turn'

def turnreport():
	print 'New Turn'
	

while(gameOn):
	playerturn = True
	while(gameBegun==0):
		intro()
		mainChoice = initvalues()
		mchosen= False
		if(mainChoice==1 and mchosen == False):
			obscurity = 2
			trials = 3
			supsci = 0
			occult = 4
			influence = 3
			unknowable = 3
			moneystart = 12000
			troopstart = 5
		elif(mainChoice==2 and mchosen == False):
			obscurity = 3
			trials = 3
			supsci = 0
			occult = 5
			influence = 2
			unknowable = 5
			moneystart = 2000
			troopstart = 5
		elif(mainChoice==3 and mchosen == False):
			obscurity = 2
			trials = 3
			supsci = 2
			occult = 0
			influence = 3
			unknowable = 0
			moneystart = 50000
			troopstart = 12
		elif(mainChoice==4 and mchosen == False):
			obscurity = 1
			trials = 2
			supsci = 3
			occult = 0
			influence = 3
			unknowable = 3
			moneystart = 50000
			troopstart=10
		elif(mainChoice==5 and mchosen == False):
			obscurity = 3
			trials = 1
			supsci = 0
			occult = 1
			influence = 4
			unknowable = 3
			moneystart=20000
			troopstart=15
		elif(mainChoice==6 and mchosen == False):
			obscurity = 2
			trials = 2
			supsci = 2
			occult = 0
			influence = 3
			unknowable = 1
			moneystart=100000
			troopstart=10
		mchosen = True
		facName = nameIt()
		player = Orgi(Faction,facName,obscurity,trials,supsci,occult,influence,unknowable)
		troops = []
		for i in range(0,troopstart):
			locallist = loadnames()
			choosen = random.randint(0,len(locallist))
			currentName = locallist[choosen]
			print "name is: "+currentName
			troops.append(Cultist(currentName,trials,occult,supsci,influence,unknowable))
		
		chaching = moneystart
		gameBegun = endSetup()
	while(playerturn):
		turnreport()
		turnchoice()
		endturn()