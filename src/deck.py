import random
from card import Card

class Deck:
	"""def __init__(self):
		self._cards = []
		for i in range(1, 14):
			self._cards.append(Card(i, "Clubs"))
			self._cards.append(Card(i, "Spades"))
			self._cards.append(Card(i, "Diamonds"))
			self._cards.append(Card(i, "Hearts"))"""
	def __init__(self):
		self._cards = []
		# clubs
		for i in range(2, 15):
			self._cards.append(Card(i, "Clubs"))
		# spades
		for i in range(2, 15):
			self._cards.append(Card(i, "Spades"))
		# diamonds
		for i in range(2, 15):
			self._cards.append(Card(i, "Diamonds"))
		# hearts
		for i in range(2, 15):
			self._cards.append(Card(i, "Hearts"))

	def shuffle(self):
		random.shuffle(self._cards)

	def show_deck(self):
		for card in self._cards:
			print(card)

	def deal_card(self):
		return self._cards.pop()
