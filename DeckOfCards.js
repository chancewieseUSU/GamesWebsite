class DeckOfCards {
    constructor() {
        this.deck = [];
        this.suits = ["Hearts", "Diamonds", "Spades", "Clubs"];
        this.faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"];
        this.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11];
        this.playIdx = 0;

        for (const suit of this.suits) {
            for (let i = 0; i < this.faces.length; i++) {
                this.deck.push({
                    suit: suit,
                    face: this.faces[i],
                    value: this.values[i]
                });
            }
        }

        this.shuffleDeck();
    }

    shuffleDeck() {
        for (let i = this.deck.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.deck[i], this.deck[j]] = [this.deck[j], this.deck[i]];
        }
        this.playIdx = 0;
    }

    getCard() {
        this.playIdx++;
        return this.deck[this.playIdx - 1];
    }
}

// Export the DeckOfCards class for use in other modules (CommonJS syntax)
module.exports = DeckOfCards;
