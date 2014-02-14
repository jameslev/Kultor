import random

gameBegun = 0

def intro(gameState):
	
	if(gameState == 0):
		turn = 0
		gameState = 2
		print 'Welcome master to our organizations annual "doomed breakfast"'
		print ''
		
		#global gameBegun
		#gameBegun = 2
		return gameState
		

while(True)	:	
	gameBegun = intro(gameBegun)
	
	