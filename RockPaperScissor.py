import random
import time

rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

playerScore = 0
computerScore = 0

def StartGame():
	print("Starting a game of Rock, Paper, Scissors.")
	while PlayGame():
		pass
	ShowScores()

def PlayGame():
	Player = GetPlayerMove()
	Computer = random.randint(1,3)
	DisplayResults(Player,Computer)
	return PlayAgain()

def GetPlayerMove():
	while True:
		print()
		Player = input("Make a Choice:\nRock = 1\nPaper = 2\nScissors = 3\nMy Choice/> ")
		try:
			Player = int(Player)
			if(Player in (1,2,3)):
				return Player
		except ValueError:
			pass
		print("Aaahh!! I didn't get that. Please enter 1, 2 or 3.")

def DisplayResults(Player,Computer):
	print("1...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("3!")
	time.sleep(0.5)
	print("Computer threw {0}".format(names[Computer]))
	global playerScore, computerScore
	if(Player == Computer):
		print("The Game is Tied.")
	else:
		if(rules[Player] == Computer):
			print("You Won this Round.")
			playerScore += 1
		else:
			print("You Lost this Round. Computer Wins!")
			computerScore += 1

def PlayAgain():
	Answer = input("Do you want to play again? Yes/No: ")
	if(Answer in ("y","Y","yes","Yes")):
		return Answer
	else:
		print("Thanks for playing. See you next time!")

def ShowScores():
	global playerScore, computerScore
	print("HIGH SCORES")
	print("Player: ",playerScore)
	print("Computer: ",computerScore)

if __name__ == "__main__":
	StartGame()