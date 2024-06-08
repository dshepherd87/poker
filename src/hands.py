import itertools
from card import Card

class Hands:
    def high_card(cards):
        cards.sort()
        return cards[-1]
        
    def pairs(cards):
        pairs = []
        for card_1, card_2 in itertools.combinations(cards, 2):
            if card_1 == card_2:
                pairs.append([card_1, card_2])
        pairs.sort()
        if len(pairs) == 1:
            return pairs[0]
        if len(pairs) > 1:
            return pairs[-1] + pairs[-2]
        else:
            return None        

    def three_of_a_kind(cards):
        sets = []
        for card_1, card_2, card_3 in itertools.combinations(cards, 3):
            if card_1 == card_2 == card_3:
                sets.append([card_1, card_2, card_3])
        sets.sort()
        if len(sets) > 0:
            return sets[-1]
        else:
            return None        
        
    def straight(cards):
        #TODO - add logic to account for Ace being both 1 and 14
        # sort the cards by rank
        cards.sort()
        # start a list for potential straights, initialized with the highest-ranking card on the table
        playable_hand = [cards[6]]

        for i in range(5, -1, -1):
            # if the card after this one in the list is one rank higher than the current card, it could be a straight. add the current card to the playable hand
            if cards[i].get_rank() + 1 == playable_hand[-1].get_rank():
                playable_hand.append(cards[i])
                if len(playable_hand) == 5:
                    playable_hand.sort()
                    return playable_hand
            # if the next-high card is more than one rank above, the straight is broken; start from scratch
            elif cards[i+1].get_rank() > cards[i].get_rank() + 1:
                playable_hand = [cards[i]]
        return None
    
    def flush(cards):
        same_suit = []
        for card_1 in cards:
            same_suit.append(card_1)
            for card_2 in cards:
                if card_1.get_suit() == card_2.get_suit() and card_1.get_rank() != card_2.get_rank():
                    same_suit.append(card_2)
            if len(same_suit) >= 5:
                same_suit.sort()
                return same_suit[-5:]
            else:
                same_suit = []
        return None
    
    def full_house(cards):
        # need to use copy of cards list to avoid changing the list for other methods
        cards_to_play = cards.copy()
        # simply use the three_of_a_kind() method to check for a set
        set = Hands.three_of_a_kind(cards_to_play)
        if set is None:
            return None
        # remove the cards that comprise the 3-of-a-kind from the cards to be considered for a pair
        for card in set:
            cards_to_play.remove(card)
        # check if there are multiple pairs on the table - if so, use the highest value pair
        pair = Hands.pairs(cards_to_play)
        if pair is not None:
            return set + pair
        # if there is both a pair and a set available, there is a full house - return it
        return None
        
    def four_of_a_kind(cards):
        playing_hand = []
        for card in cards:
            if cards.count(card) == 4:
                playing_hand.append(card)
        if len(playing_hand) == 4:
            return playing_hand
        else:
            return None        

    def straight_flush(cards):
        # same basic logic as that for the simple straight, but add the added component of the cards' suit
        # sort the cards by rank
        cards.sort()
        # start a list for potential straights, initialized with the highest-ranking card on the table
        playable_hand = [cards[6]]

        for i in range(5, -1, -1):
            # if the card after this one in the list is one rank higher than the current card, it could be a straight. add the current card to the playable hand
            if playable_hand[-1].get_rank() == cards[i].get_rank() + 1  and cards[i].get_suit() == playable_hand[0].get_suit():
                playable_hand.append(cards[i])
                if len(playable_hand) == 5:
                    playable_hand.sort()
                    return playable_hand
            # if the next-high card is more than one rank above, the straight is broken; start from scratch
            elif cards[i+1].get_rank() > cards[i].get_rank() + 1:
                playable_hand = [cards[i]]
        return None
    
    def strongest_hand(cards):
        hand = Hands.straight_flush(cards)
        if hand is not None:
            return hand
        hand = Hands.four_of_a_kind(cards)
        if hand is not None:
            return hand
        hand = Hands.full_house(cards)
        if hand is not None:
            return hand
        hand = Hands.flush(cards)
        if hand is not None:
            return hand
        hand = Hands.straight(cards)
        if hand is not None:
            return hand
        hand = Hands.three_of_a_kind(cards)
        if hand is not None:
            return hand
        hand = Hands.pairs(cards)
        if hand is not None and len(hand) == 4:
            return hand
        if hand is not None and len(hand) == 2:
            return hand
        hand = Hands.high_card(cards)
        return hand

