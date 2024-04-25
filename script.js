/*global uscore, dscore*/

document.addEventListener("DOMContentLoaded", function () {
    const startGameBtn = document.getElementById("start-game-btn");
    const hitBtn = document.getElementById("hit-btn");
    const standBtn = document.getElementById("stand-btn");
    const gameSection = document.getElementById("game-section");

    let deck = [];
    let suits = ["Hearts", "Diamonds", "Spades", "Clubs"];
    let faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"];
    let values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11];
    let playIdx = 0;

    function Card(suit, face, value) {
        this.suit = suit;
        this.face = face;
        this.val = value;
    }

    function createDeck() {
        for (let suit of suits) {
            for (let i = 0; i < faces.length; i++) {
                deck.push(new Card(suit, faces[i], values[i]));
            }
        }
        playIdx = 0;
    }

    function shuffleDeck() {
        for (let i = deck.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [deck[i], deck[j]] = [deck[j], deck[i]];
        }
        playIdx = 0;
    }

    function getCard() {
        playIdx++;
        return deck[playIdx - 1];
    }

    startGameBtn.addEventListener("click", function () {
        deck = [];
        createDeck();
        shuffleDeck();
        gameSection.innerHTML = ""; // Clear previous game content
        startGame();
    });

    function startGame() {
        let ucard = getCard();
        let ucard2 = getCard();
        let ucardnumber = 2;
        let uscore = ucard.val + ucard2.val;
        let uace = (ucard.face === "Ace" ? 1 : 0) + (ucard2.face === "Ace" ? 1 : 0);

        let dcard = getCard();
        let dcard2 = getCard();
        let dcardnumber = 2;
        let dscore = dcard.val + dcard2.val;
        let dace = (dcard.face === "Ace" ? 1 : 0) + (dcard2.face === "Ace" ? 1 : 0);

        let gameResult = "";

        hitBtn.addEventListener("click", function () {
            let ucardNew = getCard();
            ucardnumber++;
            if (ucardNew.face === "Ace") {
                uace++;
            }
            uscore += ucardNew.val;
            if (uscore > 21 && uace > 0) {
                uscore -= 10;
                uace--;
            }
            displayUserCard(ucardNew);
            displayScore(uscore);
            if (uscore >= 21) {
                endGame();
            }
        });

        standBtn.addEventListener("click", function () {
            while (dscore < 17) {
                let dcardNew = getCard();
                dcardnumber++;
                if (dcardNew.face === "Ace") {
                    dace++;
                }
                dscore += dcardNew.val;
                if (dscore > 21 && dace > 0) {
                    dscore -= 10;
                    dace--;
                }
                displayDealerCard(dcardNew);
                displayScore(dscore);
            }
            endGame();
        });
    }

    function displayUserCard(card) {
        let cardText = `${card.face} of ${card.suit}`;
        let cardElement = document.createElement("div");
        cardElement.textContent = cardText;
        gameSection.appendChild(cardElement);
    }

    function displayDealerCard(card) {
        let cardText = `${card.face} of ${card.suit}`;
        let cardElement = document.createElement("div");
        cardElement.textContent = cardText;
        gameSection.appendChild(cardElement);
    }

    function displayScore(score) {
        let scoreElement = document.createElement("div");
        scoreElement.textContent = `Score: ${score}`;
        gameSection.appendChild(scoreElement);
    }

    function endGame() {
        let resultElement = document.createElement("div");
        if (uscore > 21) {
            resultElement.textContent = "User busted, you lose!";
        } else if (dscore > 21) {
            resultElement.textContent = "The dealer busted, you win!";
        } else if (dscore >= uscore) {
            resultElement.textContent = "The dealer wins!";
        } else {
            resultElement.textContent = "You win!";
        }
        gameSection.appendChild(resultElement);
    }
});
