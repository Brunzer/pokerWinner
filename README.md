# PokerWinner

pokerWinner.py is a program that determines the winning 5-card poker hand from two hands supplied.

###### pokerWinner.py
Contains two functions:

Main()
  - A function to gather input from user and check if card hands are valid|

findWinner()
  - takes in two strings as parameters, which are the poker hands
  - calls upon functions from imported module handeval.py, which includes multiple functions to compare hands for particular winning hands (ie. Full House, 3 of a kind, etc)
  - returns the winning hand as a string based on the hand that had the higher rank


###### handeval.py 
Contains a class "Evaluate" with multiple functions that determine what the possible hand is that was passed in. A rank is supplied to the hand, depending on what hand type is determined.

Input parameters are taken in as strings, with each card in the hand separated by a blank space. A card consists of a combination of a rank and a suit, each is 1 char (ie. 4D is a 4 of diamonds).
Full list of ranks:
	- 2-9 are as is, T for 10, J for Jack, Q for Queen, K for King, and A for Ace.
Full list of suits:
	- C for Clubs, D for Diamonds, H for Hearts, S for Spades.

You could install the pokerWinner modules if you see fit, though I suggest you setup a virtual python environment if you decide to do so. Once that's setup, you can run 'python setup.py install' to install the pokerWinner modules.

### RUNNING THE CODE
###### Run pokerWinner.py from command line without installing modules:
Here you will be asked to provide each players cards with keyboard input prompts

```bash
	$ python pokerWinner.py
	Enter Player 1's Hand: 
	5H 7D 9C 9S TD
	Enter Player 2's Hand: 
	QH 4D QS TD KS
	Winning hand is QH 4D QS TD KS
```

###### Passing hands directly to function on command line:
Here you can pass the hand strings directly to the findWinner function
```bash
	$ python -c "import pokerWinner; print pokerWinner.findWinner('9C 6H 3D TC 5C', '5H QD 6H 7C 7D')"
	5H QD 6H 7C 7D
```

### RUNNING TESTS
tests/pokerTests.py imports the unittest python module and runs through multiple functions to test appropriate output from the program.

To run these tests, use either unittest or nosetests (make sure you have these installed already. If not you can install these using pip)

###### Using unittests from the top pokerWinner dir:
```bash
$ python -m unittest -v pokerWinner.tests.pokerTests
```

###### Using nosetests from the top pokerWinner dir:
```bash
$ nosetests -v pokerWinner.tests.pokerTests
```
