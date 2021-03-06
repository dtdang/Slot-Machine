import random
from enum import Enum
import tkinter as tk


class SlotMachine:
	def __init__(self, money=10):
		self.money = money

	class Symbols(Enum):
		ACE = 1
		KING = 2
		QUEEN = 3
		JACK = 4
		JOKER = 5
		HEART = 6
		SPADE = 7
		CLOVER = 8
		DIAMOND = 9
		

	@property
	def __continue_playing(self):
		answer = ''
		cancel = ["Quit", "quit", "quit ", "q"]
		play = ["Play", "play", "PLAY", "p", "play ", "P"]
		while True:
			try:
				print(f"You have ${self.money} left in your wallet.")
				answer = input("Play the slots? [Quit or Play]: ")
			except ValueError:
				continue
			else:
				break
		if answer in cancel:
			return False
		elif answer in play:
			return True
	
	def __play_round(self):
		#Roll slots
		choices = [symbols.name for symbols in SlotMachine.Symbols]
		first, second, third = random.choice(choices), random.choice(choices), random.choice(choices)
		stars = 12 + len(first) + len(second) + len(third)
		print(f"""	
{'*'*stars}
*** {first} -- {second} -- {third} ***
{'*'*stars}
		""")
		self.__check_rolls(first, second, third)
		
	def __check_rolls(self, first, second, third):
	#Check to see if rolls match
		if first == second == third and first == "ACE":
			self.money += 500
			print("You matched all Hearts... you win $50\n")
		elif first == second == third:
			self.money += 50
			print("You matched 3 symbols... you win $5\n")
		elif first == second or first == third or second == third:
			self.money += 20
			print("You matched 2 symbols... you win $2\n")
		else:
			print("L-O-S-E-R")
		print(f"{'-'*35}")

	def play(self):
	#Check for money and check continue playing else exit
		question = True
		while True:
			if self.money >= 2 and question:
				question = self.__continue_playing
				if question:
					self.money -= 20
					self.__play_round()
			else:
				print("\nThanks for playing!")
				break


if __name__ == '__main__':
	print(f"""
Welcome to SlotMachine v0.1
{'-'*40}
It costs $2 to play.
If all 3 reels match, you get $5.
If all 3 reels are HEARTS, you get $50!
If 2 reels match, you get $2.
Otherwise... you get nothing!

{'-'*40}
	""")
	# for symbol in SlotMachine.Symbols:
	# 	print(symbol.name)
	SlotMachine().play()
'''
Next  things to add:
	-Change odds
	-More icons and different payouts
	-use graphics for rolls
	-multiple lanes
	-GUI with tkinter
'''

