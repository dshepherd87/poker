import unittest

from player import Player
from card import Card
from hands import Hands

class TestHands(unittest.TestCase):
    def test_high_card(self):
        player_1 = Player("Player_1", 10)
        player_1.add_card(Card(10,"Spades"))
        player_1.add_card(Card(4, "Clubs"))

        high_Card = Hands.high_card(player_1.get_hand())

    def test_pairs(self):
        # test one pair
        cards_2 = [Card(9, "Clubs"), Card(3, "Diamonds"), Card(2, "Hearts"), Card(7, "Spades"), Card(14, "Clubs"), Card(10, "Diamonds"), Card(14, "Hearts")]
        hand_2 = Hands.pairs(cards_2)
        self.assertEqual(hand_2, [Card(14, "Clubs"), Card(14, "Hearts")])
        # test two-pair
        cards_1 = [Card(9, "Clubs"), Card(3, "Diamonds"), Card(3, "Hearts"), Card(7, "Spades"), Card(14, "Clubs"), Card(7, "Diamonds"), Card(14, "Hearts")]
        hand_1 = Hands.pairs(cards_1)
        self.assertEqual(hand_1, [Card(14, "Clubs"), Card(14, "Hearts"), Card(7, "Spades"), Card(7, "Diamonds")])


    def test_three_of_a_kind(self):
        #cards = [Card(3, "Diamonds"), Card(1, "Spades"), Card(9, "Clubs"), Card(9, "Diamonds"), Card(3, "Hearts"), Card(9, "Spades"), Card(3, "Spades")]
        cards = [Card(14, "Diamonds"), Card(6, "Clubs"), Card(6, "Hearts"), Card(10, "Spades"), Card(14, "Hearts"), Card(6, "Spades"), Card(3, "Diamonds")]
        set = Hands.three_of_a_kind(cards)
        self.assertEqual(set, [Card(6, "Clubs"), Card(6, "Hearts"), Card(6, "Spades")])

    def test_straight(self):
        cards = [Card(6, "Diamonds"), Card(14, "Spades"), Card(9, "Clubs"), Card(3, "Diamonds"), Card(8, "Hearts"), Card(10, "Spades"), Card(7, "Clubs")]
        hand = Hands.straight(cards)
        self.assertEqual(hand, [Card(6, "Diamonds"), Card(7, "Clubs"), Card(8, "Hearts"), Card(9, "Clubs"), Card(10, "Spades")])        

    def test_flush(self):
        cards = [Card(14, "Spades"), Card(4, "Diamonds"), Card(5, "Diamonds"), Card(9, "Diamonds"), Card(3, "Diamonds"), Card(14, "Diamonds"), Card(14, "Clubs")]
        hand = Hands.flush(cards)
        self.assertEqual(hand, [Card(3, "Diamonds"), Card(4, "Diamonds"), Card(5, "Diamonds"), Card(9, "Diamonds"), Card(14,"Diamonds")])    

    def test_full_house(self):
        cards = [Card(14, "Diamonds"), Card(6, "Clubs"), Card(6, "Hearts"), Card(10, "Spades"), Card(14, "Hearts"), Card(6, "Spades"), Card(3, "Diamonds")]
        hand = Hands.full_house(cards)
        self.assertEqual(hand, [Card(6, "Clubs"), Card(6, "Hearts"), Card(6, "Spades"), Card(14, "Diamonds"), Card(14, "Hearts")])

    def test_four_of_a_kind(self):
        cards = [Card(9, "Diamonds"), Card(14, "Spades"), Card(9, "Clubs"), Card(4, "Diamonds"), Card(9, "Hearts"), Card(9, "Spades"), Card(14, "Clubs")]
        set = Hands.four_of_a_kind(cards)
        self.assertEqual(set, [Card(9, "Diamonds"), Card(9, "Hearts"), Card(9, "Spades"), Card(9, "Clubs")])

    def test_straight_flush(self):
        cards = [Card(6, "Clubs"), Card(14, "Spades"), Card(9, "Clubs"), Card(9, "Diamonds"), Card(8, "Clubs"), Card(10, "Clubs"), Card(7, "Clubs")]
        hand = Hands.straight_flush(cards)
        self.assertEqual(hand, [Card(6, "Clubs"), Card(7, "Clubs"), Card(8, "Clubs"), Card(9, "Clubs"), Card(10, "Clubs")])           

    def test_strongest_hand(self):
        # if strongest hand is a pair
        cards_pair = [Card(11, "Clubs"), Card(4, "Diamonds"), Card(13, "Spades"), Card(4, "Hearts"), Card(8, "Clubs"), Card(14, "Diamonds"), Card(3, "Diamonds")]
        hand_pair = Hands.strongest_hand(cards_pair)
        self.assertEqual(hand_pair, [Card(4, "Diamonds"), Card(4, "Hearts")])

        # strongest hand is two-pair
        cards_two_pair = [Card(11, "Clubs"), Card(4, "Diamonds"), Card(14, "Spades"), Card(4, "Hearts"), Card(8, "Clubs"), Card(14, "Diamonds"), Card(3, "Diamonds")]
        hand_two_pair = Hands.strongest_hand(cards_two_pair)
        self.assertEqual(hand_two_pair, [Card(14, "Spades"), Card(14, "Diamonds"), Card(4, "Diamonds"), Card(4, "Hearts")])

        # strongest hand is three-of-a-kind
        cards_3_of_a_kind = [Card(11, "Clubs"), Card(4, "Diamonds"), Card(13, "Spades"), Card(4, "Hearts"), Card(8, "Clubs"), Card(14, "Diamonds"), Card(4, "Spades")]
        hand_3_of_a_kind = Hands.strongest_hand(cards_3_of_a_kind)
        self.assertEqual(hand_3_of_a_kind, [Card(4, "Diamonds"), Card(4, "Hearts"), Card(4, "Spades")])

        # strongest hand is a straight
        cards_straight = [Card(10, "Hearts"), Card(7, "Clubs"), Card(2, "Spades"), Card(8, "Diamonds"), Card(11, "Hearts"), Card(4, "Spades"), Card(9, "Spades")]
        hand_straight = Hands.strongest_hand(cards_straight)
        self.assertEqual(hand_straight, [Card(7, "Clubs"), Card(8, "Diamonds"), Card(9, "Spades"), Card(10, "Hearts"), Card(11, "Hearts")])

        # strongest hand is a flush
        cards_flush = [Card(11, "Diamonds"), Card(4, "Diamonds"), Card(14, "Spades"), Card(4, "Hearts"), Card(8, "Diamonds"), Card(14, "Diamonds"), Card(3, "Diamonds")]
        hand_flush = Hands.strongest_hand(cards_flush)
        self.assertEqual(hand_flush, [Card(3, "Diamonds"), Card(4, "Diamonds"), Card(8, "Diamonds"), Card(11, "Diamonds"), Card(14, "Diamonds")])

        # strongest hand is a full house
        cards_full_house = [Card(5, "Diamonds"), Card(11, "Hearts"), Card(7, "Clubs"), Card(5, "Clubs"), Card(11, "Spades"), Card(3, "Diamonds"), Card(5, "Hearts")]
        hand_full_house = Hands.strongest_hand(cards_full_house)
        self.assertEqual(hand_full_house, [Card(5, "Diamonds"), Card(5, "Clubs"), Card(5, "Hearts"), Card(11, "Hearts"), Card(11, "Spades")])

        # strongest hand is four of a kind
        cards_4_of_a_kind = [Card(10, "Hearts"), Card(7, "Diamonds"), Card(10, "Spades"), Card(10, "Clubs"), Card(12, "Spades"), Card(10, "Diamonds"), Card(4, "Spades")]
        hand_4_of_a_kind = Hands.strongest_hand(cards_4_of_a_kind)
        self.assertEqual(hand_4_of_a_kind, [Card(10, "Hearts"), Card(10, "Spades"), Card(10, "Clubs"), Card(10, "Diamonds")])

        # strongest hand is straight flush
        cards_straight_flush = [Card(10, "Clubs"), Card(7, "Clubs"), Card(2, "Spades"), Card(8, "Clubs"), Card(11, "Clubs"), Card(4, "Spades"), Card(9, "Clubs")]
        hand_straight_flush = Hands.strongest_hand(cards_straight_flush)
        self.assertEqual(hand_straight_flush, [Card(7, "Clubs"), Card(8, "Clubs"),Card(9, "Clubs"),Card(10, "Clubs"),Card(11, "Clubs")])

if __name__ == "__main__":
    unittest.main()