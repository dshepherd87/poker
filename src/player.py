from hands import Hands

class Player:
	def __init__(self, name, stack):
		self._name = name
		self._stack = stack
		self._hand = []
		self.is_dealer = False

	def __repr__(self):
		return self._name
	
	#def __eq__(self, other):
	#	return self._name == other._name

	def get_hand(self):
		return self._hand

	def give_chips(self, chips):
		self._stack += chips

	def take_chips(self, chips):
		if self._stack - chips>= 0:
			self._stack -= chips
		else:
			raise Exception("Player cannot go negative on stack")

	def add_card(self, new_card):
		self._hand.append(new_card)

	def set_is_dealer(self):
		self.is_dealer = True

	def unset_is_dealer(self):
		self.is_dealer = False

	def best_available_hand(self, board):
		cards = self._hand + board
		best_hand = Hands.straight_flush(cards)
		if best_hand is not None and best_hand[4].get_value() == 14:
			return best_hand, "Royal Flush"
		if best_hand is not None:
			return best_hand, "Straight Flush"
		best_hand = Hands.four_of_a_kind(cards)
		if best_hand is not None:
			return best_hand, f"Four {best_hand[0].get_suit()}"
		best_hand = Hands.full_house(cards)
		
