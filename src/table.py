from deck import Deck
from card import Card
from player import Player

class Table:
	def __init__(self, num_seats):
		self.board = []
		#self.deck = Deck()
		self._num_seats = num_seats
		self._seats = {}	
		for i in range(self._num_seats):
			self._seats[f"Seat {i+1}"] = None
	
	def deal_card_to_board(self, card):
		self._board.append(card)

	def return_num_seats(self):
		return self._num_seats

	def seat_player(self, player):
		# make sure that there is at least one empty seat
		if None not in self._seats.values():
			raise Exception("The table is full, no additional players may be seated")
		# seat the player in the first available seat
		for seat in self._seats:
			if self._seats[seat] is None:
				self._seats[seat] = player
				break
	
	def unseat_player(self, player):
		if player not in self._seats.values():
			raise Exception(f"{player} is not seated at the table")
		# identify where the player is seated 		
		seat_to_vacate = list(self._seats.keys())[list(self._seats.values()).index(player)]
		# reset the occupent of the seat to None
		self._seats[seat_to_vacate] = None
