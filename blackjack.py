import random      #brings in random for shuffling
import json
import requests

class Card(): #creates cards class
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.val = value
        
    def __str__(self):
        return self.face + " of " + self.suit + ", value: " + str(self.val)
        
    def to_dict(self):
        return {
            'suit': self.suit,
            'face': self.face,
            'value': self.val
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class DeckOfCards():    #creates deck of cards class
    def __init__(self):
        self.deck = []
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.play_idx = 0
        
        for suit in self.suits:
            i = 0
            for i in range(len(self.faces)):
                self.deck.append(Card(suit, self.faces[i], self.values[i]))
                
                
    def shuffle_deck(self):     #allows us to shuffle deck
        random.shuffle(self.deck)
        self.play_idx = 0
        
    def print_deck(self):       #allows us to print deck
        for card in self.deck:
            print(card.face, "of", card.suit, end=", ")
        print("---")
        
    def get_card(self):     #allows us to get a card from the deck
        self.play_idx += 1
        return self.deck[self.play_idx - 1]
        
    def to_dict(self):
        return {
            'deck': self.deck,
            'suits': self.suits,
            'faces': self.faces,
            'values': self.values,
            'play_idx': self.play_idx
        }
        
    @classmethod
    def from_dict(cls, data):
        deck_obj = cls()  # Create a new instance of the class

        # Set attributes based on dictionary values
        deck_obj.deck = data['deck']
        deck_obj.suits = data['suits']
        deck_obj.faces = data['faces']
        deck_obj.values = data['values']
        deck_obj.play_idx = data['play_idx']

        return deck_obj

def initialize_blackjack():
    # Initialize game variables
    uscore = 0
    dscore = 0
    uwincount = 0
    dwincount = 0
    return uscore, dscore, uwincount, dwincount

def deal_initial_blackjack_cards(deck):
    # Deal initial cards to the player and dealer
    ucard = deck.get_card()
    ucard2 = deck.get_card()
    dcard = deck.get_card()
    dcard2 = deck.get_card()
    return ucard, ucard2, dcard, dcard2

def calculate_blackjack_score(cards):
    # Calculate the score for a set of cards
    score = sum(card.val for card in cards)
    return score
    
def calculate_ace_count(cards):
    # Calculate the number of Aces in a set of cards
    ace_count = sum(1 for card in cards if card.face == "Ace")
    return ace_count
    
# def update_hitstand(hitstand, value):
#     hitstand = value
#     return hitstand

# def play_blackjack():
#     uscore, dscore, uwincount, dwincount = initialize_blackjack()
#     outputs = {}  # Initialize an empty dictionary to store outputs
#     playagain = 'y'
#     while playagain == 'y':
#         deck = DeckOfCards()    # Create a new deck for each game
#         deck.shuffle_deck()
        
#         ucard, ucard2, dcard, dcard2 = deal_initial_blackjack_cards(deck)
#         ucardnumber = 2
#         dcardnumber = 2
        
#         uace = calculate_ace_count([ucard, ucard2])
#         dace = calculate_ace_count([dcard, dcard2])
        
#         uscore = calculate_blackjack_score([ucard, ucard2])
#         dscore = calculate_blackjack_score([dcard, dcard2])
        
#         outputs['ucard'] = "Card number 1 is: " + ucard.face + " of " + ucard.suit + "<br>"
#         outputs['ucard2'] = "Card number 2 is: " + ucard2.face + " of " + ucard2.suit + "<br><br>"
#         outputs['uscore'] = "Your score is: " + str(uscore) + "<br>"
        
#         hitstand = 'h'
#         while hitstand == 'h' and uscore < 21:
#             hitstand = input("button for site")
#             if hitstand == 'h':
#                 ucard_new = deck.get_card()
#                 ucardnumber += 1
#                 outputs['ucard_new'] = "Card number " + str(ucardnumber) + " is: " + ucard_new.face + " of " + ucard_new.suit + "<b>"
#                 if ucard_new.face == "Ace":
#                     uace += 1
#                 uscore += ucard_new.val
#                 if uscore > 21 and uace > 0:
#                     uscore -= 10
#                     uace -= 1
#                 outputs['uscore'] = "Your score is: " + str(uscore) + "<br>"
#             elif hitstand == 's':
#                 break
        
        
        
#         playagain = 'n'  # For testing purposes, set to 'n' to exit the loop after one round

#     return outputs

        
        
# #             
#                 print("Card drawn:", ucard_new.face, "of", ucard_new.suit) # I'd like to display this new card after they click their button
#                 uscore += ucard_new.val
#                 print("Your new score is:", uscore) # Display this after the new card
#                 if uscore > 21:
#                     print("You busted! Dealer wins.") #display this if it meets the logic
#                     dwincount += 1
#                     break
#             elif action == 's':
#                 while dscore < 17:
#                     dcard_new = deck.get_card()
#                     dscore += dcard_new.val
#                 print("Dealer's score is:", dscore) # I'd like to display this on the site as well
#                 if dscore > 21 or uscore > dscore:
#                     print("You win!")       # I'd like to display this on the site as well
#                     uwincount += 1
#                 elif dscore > uscore:
#                     print("Dealer wins!")       # I'd like to display this on the site as well
#                     dwincount += 1
#                 else:
#                     print("It's a tie!")        # I'd like to display this on the site as well
#                 break
#             else:
#                 print("Invalid input. Please enter 'h' for hit or 's' for stand.")      # I'd like to display this on the site as well

#         playagain = input("\nWould you like to play again? (y/n): ")    # I'd like to display this on the site as well, and two buttons should now appear that say "yes" or "no" which assign playagain a value of 'y' or 'n'
    
#     print("\n\nUser win count:", uwincount) # I'd like to display this on the site as well
#     print("Dealer win count:", dwincount)   # I'd like to display this on the site as well
#     if uwincount > dwincount:
#         print("You are the overall winner!")    # I'd like to display this on the site as well
#     elif dwincount > uwincount:
#         print("The dealer is the overall winner!")  # I'd like to display this on the site as well
#     else:
#         print("It's a tie!")    # I'd like to display this on the site as well
#     print("\n\nThanks for playing!")    # I'd like to display this on the site as well




# play_blackjack()
