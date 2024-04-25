const DeckOfCards = require('./DeckOfCards.js');

function initializeBlackjack() {
    // Initialize game variables
    let uscore = 0;
    let dscore = 0;
    let uwincount = 0;
    let dwincount = 0;
    return [uscore, dscore, uwincount, dwincount];
}

function dealInitialBlackjackCards(deck) {
    // Deal initial cards to the player and dealer
    const ucard = deck.getCard();
    const ucard2 = deck.getCard();
    const dcard = deck.getCard();
    const dcard2 = deck.getCard();
    return [ucard, ucard2, dcard, dcard2];
}

function calculateBlackjackScore(cards) {
    // Calculate the score for a set of cards
    const score = cards.reduce((total, card) => total + card.val, 0);
    return score;
}

function playBlackjack() {
    let [uscore, dscore, uwincount, dwincount] = initializeBlackjack();
    let playagain = 'y';
    while (playagain.toLowerCase() === 'y') {
        const deck = new DeckOfCards(); // Create a new deck for each game
        deck.shuffleDeck();

        const [ucard, ucard2, dcard, dcard2] = dealInitialBlackjackCards(deck);

        uscore = calculateBlackjackScore([ucard, ucard2]);
        dscore = calculateBlackjackScore([dcard, dcard2]);

        // Your game logic for hitting, standing, and determining the winner goes here
        while (uscore <= 21) {
            const action = prompt("Would you like to hit or stand? (h/s): ");
            if (action && action.toLowerCase() === 'h') {
                const ucardNew = deck.getCard();
                console.log("Card drawn:", ucardNew.face, "of", ucardNew.suit);
                uscore += ucardNew.val;
                console.log("Your new score is:", uscore);
                if (uscore > 21) {
                    console.log("You busted! Dealer wins.");
                    dwincount++;
                    break;
                }
            } else if (action && action.toLowerCase() === 's') {
                while (dscore < 17) {
                    const dcardNew = deck.getCard();
                    dscore += dcardNew.val;
                }
                console.log("Dealer's score is:", dscore);
                if (dscore > 21 || uscore > dscore) {
                    console.log("You win!");
                    uwincount++;
                } else if (dscore > uscore) {
                    console.log("Dealer wins!");
                    dwincount++;
                } else {
                    console.log("It's a tie!");
                }
                break;
            } else {
                console.log("Invalid input. Please enter 'h' for hit or 's' for stand.");
            }
        }

        playagain = prompt("\nWould you like to play again? (y/n): ");
    }

    console.log("\n\nUser win count:", uwincount);
    console.log("Dealer win count:", dwincount);
    if (uwincount > dwincount) {
        console.log("You are the overall winner!");
    } else if (dwincount > uwincount) {
        console.log("The dealer is the overall winner!");
    } else {
        console.log("It's a tie!");
    }
    console.log("\n\nThanks for playing!");
}

// Entry point
console.log("Welcome to BlackJack!\n");
playBlackjack();
