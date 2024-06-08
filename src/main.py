from card import Card
from deck import Deck
from table import Table
from game import Game
from player import Player
from hands import Hands

def main():
        board = [Card(9, "Clubs"), Card(9, "Diamonds"), Card(8, "Clubs"), Card(10, "Clubs"), Card(7, "Clubs")]
        player = Player("Player", 0)
        player.add_card(Card(6, "Clubs"))
        player.add_card(Card(1, "Spades"))

        hand = Hands.straight_flush(player, board)        

main()
