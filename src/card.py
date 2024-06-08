class Card:
	def __init__(self, rank, suit):
		self._rank = rank
		self._suit = suit
		if self._rank == 14:
			self._name = f"Ace of {self._suit}"
			self._shorthand = f"A{self._suit[0].lower()}"
		elif self._rank == 11:
			self._name = f"Jack of {self._suit}"
			self._shorthand = f"J{self._suit[0].lower()}"
		elif self._rank == 12:
			self._name = f"Queen of {self._suit}"
			self._shorthand = f"Q{self._suit[0].lower()}"
		elif self._rank == 13:
			self._name = f"King of {self._suit}"
			self._shorthand = f"K{self._suit[0].lower()}"
		else:
			self._name = f"{self._rank} of {self._suit}"
			self._shorthand = f"{self._rank}{self._suit[0].lower()}"

	# use the name string to represent each card, eg. Ace of Clubs
	def __repr__(self):
		return self._name

	# check if two cards are of equal rank
	def __eq__(self, other):
		return self._rank == other._rank

	# compare if the rank of one card is greater than that of another	
	def __gt__(self, other):
		#special logic needed to compare Ace
		#if self._rank == 1 and not other._rank == 1:
		#	return True
		#if other._rank == 1 and not self._rank == 1:
		#	return False
		# if neither card is an ace, basic integer logic applies
		return self._rank > other._rank

	# compare if the rank of one card is less than that of another	
	def __lt__(self, other):
		#special logic needed to compare Ace
		#if self._rank == 1 and not other._rank == 1:
		#	return False
		#if other._rank == 1 and not self._rank == 1:
		#	return True
		# if neither card is an ace, basic integer logic applies
		return self._rank < other._rank

	# return the rank of the Card object	
	def get_rank(self):
		return self._rank

	# return the suit of the Card object
	def get_suit(self):
		return self._suit