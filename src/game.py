from card import Card
from deck import Deck
from table import Table

class Game:
	def __init__(self, table, players, small_blind, big_blind, hand_size=2):
		self._table = table
		self._players = players
		
		self._small_blind = small_blind
		self._big_bling = big_blind
		self._deck = Deck()
		self._deck.shuffle()
		self._hand_size = hand_size
		self._board = []
		self._pot = 0

	def add_player(self, player):
		if len(self._players) == self._table.return_num_seats:
			raise Exception("The table is already full, no more players may be seated")
		if player in self._players:
			raise Exception(f"A player named {player} is already in this game")
		self._players.append(player)
		self._table.seat_player(player)

	def remove_player(self, player):
		self._players.remove(player)
		self._table.unseat_player(player)

	def deal_to_players(self):
		# the number of cards to be dealt to each player depends on the form of Poker being played
		for i in range(self._hand_size):
			# cycle through each player to deal the cards
			for player in self._players:
				player.add_card(self._deck.deal_card())

	def deal_flop(self):
		for i in range(3):
			self._board.append(self._deck.deal_card())

	def deal_turn(self):
		self._board.append(self._deck.deal_card())

	def deal_river(self):
		self._board.append(self._deck.deal_card())
		
	def add_to_pot(self, player, bet):
		self._pot += bet
		player.bet(bet)

	def check_high_card(players):
		# create list for the high cards of each player
		high_cards = []
		# retriece the high card from each player's hand
		for player in players:
			high_cards.append(max(player._hand))
		# get the index for the card with the highest rank
		index_max = max(range(len(high_cards)), key=high_cards.__getitem__)
		#return the player with the matching list index
		return players[index_max]

	def high_card(players):
        #the hand that will be passed in is the combination of theh player's own cards, and the community cards
		high_cards = []
		for player in players:
			high_cards.append(max(player.get_hand()))
		index_of_high_card = max(range(len(high_cards)), key=high_cards.__getitem__)

		winner = players[index_of_high_card]
		winning_card = max(winner.get_hand())
		return winner, winning_card

	def game_loop(self):
		self._players[0].set_is_dealer()
		print("Welcome to the Poker alpha test!")
		print("The current players are:")
		for player in self._players:
			if player.is_dealer == True:
				print(f"{player} (Dealer)")
			else:
				print(player)
		response = input("Shall we begin the game? (y/n): ")
		while response not in ["Y", "y", "N", "n"]:
			response = input("Invalid response, please enter a 'y' or a 'n': ")
		if response in ["N", "n"]:
			print("Exiting...")
			quit()
		print("The game is Texas Hold'em. Dealing the cards...")
		self.deal_to_players()
		print("The players have: ")
		for player in self._players:
			print(f"{player}: {player.get_hand()}")

		print("Dealing the Flop:")
		self.deal_flop()
		print(f"The community cards are: {self._board}")

		print("Dealing the Turn:")
		self.deal_turn()
		print(f"The community cards are: {self._board}")

		print("Dealing the River:")
		self.deal_river()
		print(f"The community cards are: {self._board}")