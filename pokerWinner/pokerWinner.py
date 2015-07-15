#! /usr/bin/local/python3
from handeval import Evaluate #Module I created to calculate a rank for a given hand
from sys import stdin #Public standard library for system input (only used if main function called for command line)

def isValidHand(hand):
	#Check if hand has 5 distinct cards
	if len(set(hand)) != 5:
		return False
	else:
		return True

def findWinner(hand1, hand2):
	#Turn hand strings into lists
	h1 = hand1.split()
	h2 = hand2.split()
	if not isValidHand(h1):
		return("ERROR: %s is not a valid hand" % hand1)
	if not isValidHand(h2):
		return("ERROR: %s is not a valid hand" % hand2)
	
	#Calculate hand ranks
	e = Evaluate()
	hand1Rank = e.handValue(hand1.split())
	hand2Rank = e.handValue(hand2.split())

	#Determine which hand has a higher rank
	if hand2Rank > hand1Rank:
		return hand2
	elif hand1Rank > hand2Rank:
		return hand1
	elif hand1Rank == hand2Rank:
		#If there's a tie in ranks, run a tie breaker (highest cards value)
		return ' '.join(e.tieBreaker(hand1.split(), hand2.split(), hand1Rank))

def Main():
	#Get Player 1's hand from stdin
	print("Enter Player 1's Hand: ")
	hand1 = stdin.readline()

	#Get player 2's hand from stdin
	print("Enter Player 2's Hand: ")
	hand2 = stdin.readline()
	#Print the winning hand
	print("Winning hand is %s" % findWinner(hand1, hand2))

if __name__ == "__main__":
    Main()