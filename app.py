# http://52.53.212.40:5000/
# flask run --host=0.0.0.0

from flask import Flask, render_template, redirect, url_for, request, jsonify
from blackjack import * 


class CardJSONEncoder(json.JSONEncoder):
 def default(self, obj):
  if isinstance(obj, Card):
   return obj.to_dict()  # Assuming Card has a to_dict() method
  return super().default(obj)



app = Flask(__name__, template_folder='templates', static_folder='static')
app.json_encoder = CardJSONEncoder




@app.route("/")
def home():
 return render_template('index.html')


@app.route("/eight_ball")
def eight_ball():
 return render_template('eight_ball.html')
 
 
 
 
@app.route('/blackjack', methods=['GET', 'POST'])
def blackjack():

 
 return render_template('blackjack.html')




def initialize_game():
 deck = DeckOfCards()
 deck.shuffle_deck()
 
 ucard, ucard2, dcard, dcard2 = deal_initial_blackjack_cards(deck)
 ucardnumber = 2
 dcardnumber = 2
 
 uace = calculate_ace_count([ucard, ucard2])
 dace = calculate_ace_count([dcard, dcard2])
 
 uscore = calculate_blackjack_score([ucard, ucard2])
 dscore = calculate_blackjack_score([dcard, dcard2])
 
 return deck, ucard, ucard2, dcard, dcard2, ucardnumber, dcardnumber, uace, dace, uscore, dscore






@app.route('/start-game', methods=['GET', 'POST'])
def start_game():
 # Initialize the game and retrieve game-related variables
 deck, ucard, ucard2, dcard, dcard2, ucardnumber, dcardnumber, uace, dace, uscore, dscore = initialize_game()
 serialized_deck = json.dumps(deck.to_dict(), cls=CardJSONEncoder)

 # Create the data dictionary
 data = {
  'ucard': ucard,
  'ucard2': ucard2,
  'dcard': dcard,
  'dcard2': dcard2,
  'ucardnumber': ucardnumber,
  'dcardnumber': dcardnumber,
  'uace': uace,
  'dace': dace,
  'uscore': uscore,
  'dscore': dscore
  # Add other variables as needed
 }
 
 # Render the template with the game-related data
 return render_template('blackjack_start.html', **data, deck=serialized_deck)
 

 

@app.route('/hit-or-stand', methods=['POST'])
def hit_or_stand():
 serialized_deck = request.form.get('deck')
 deck_data = json.loads(serialized_deck)
 deck = DeckOfCards.from_dict(deck_data)
 
 hit_stand_choice = request.form.get('hitstand')
 if hit_stand_choice == 'h':
  hit_stand_choice = "hit"
  ucard_new = deck.get_card()
  ucardnumber += 1
  uscore += ucard_new.val
  if ucard_new.face == "Ace":
   uace += 1
  if uscore > 21 and uace > 0:
   uscore -= 10
   uace -= 1
  
  
  
 elif hit_stand_choice == 's':
  hit_stand_choice = "stand"
 
 
 deck = deck.to_dict()
 ucard = ucard.to_dict()
 ucard2 = ucard2.to_dict()
 dcard = dcard.to_dict()
 dcard2 = dcard2.to_dict()
 ucard_new = ucard_new.to_dict()
 
 
 
 data = {
  'deck': deck,
  'ucard': ucard,
  'ucard2': ucard2,
  'dcard': dcard,
  'dcard2': dcard2,
  'ucardnumber': ucardnumber,
  'dcardnumber': dcardnumber,
  'uace': uace,
  'dace': dace,
  'uscore': uscore,
  'dscore': dscore,
  'ucard_new': ucard_new,
  'hit_stand_choice': hit_stand_choice
  # Add other variables as needed
  }
 
 
 return render_template('blackjack_hit_stand.html', **data)
 #
 #
 #
 #
 #
 #
 #
 #
 #
 #




if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)



