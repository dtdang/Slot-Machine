import random
from enum import Enum


class SlotMachine:
	def __init__(self, money=10):
		self.money = money

	class Symbols(Enum):
		HEART = 1
		DIAMOND = 2
		SPADE = 3
		CLOVER = 4

	def __continue_playing(self):
		cancel = ["Quit", "quit", "quit ", "q"]
		play = ["Play", "play", "PLAY", "p", "play "]
		while True:
			try:
				print(f"You have ${self.money} left in your wallet.")
				answer = input("Play the slots? [Quit or Play]")
			except ValueError:
				continue
			else:
				break
		if answer in cancel:
			return False
		elif answer in play:
			return True
	
	def __play_round(self):
		choices = list(SlotMachine.Symbols)
		first, second, third = random.choice(choices), random.choice(choices), random.choice(choices)

		roll = f"""	
		{'*'*60}
		*** {first} -- {second} -- {third} ***
		{'*'*60}
		"""
		print(roll)
		self.__check_rolls(first, second, third)
		
	def __check_rolls(self, first, second, third):
		if first == second == third and first == "HEART":
			self.money += 50
			print("You matched all Hearts... you win $50")
		elif first == second == third:
			self.money += 5
			print("You matched 3 symbols... you win $5")
		elif first == second or first == third or second == third:
			self.money += 2
			print("You matched 2 symbols... you win $2")

	def play(self):
		if self.money >= 2:
			question = self.__continue_playing()
			if question:
				self.money -= 2
				self.__play_round()
			else:
				print("Thanks for Playing!")
		else:
			print("YOu are out of money. Thanks for playing")


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
	SlotMachine().play()
