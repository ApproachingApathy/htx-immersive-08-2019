//Player is used interchangable with player and dealer unless otherwise specified.

function setup() {
    fiftyTwoDeck = [
        {amount:1, imgLink:"images/PNG-cards-1.3/ace_of_spades.png", face:"Ace", },
        {amount:1, imgLink:"images/PNG-cards-1.3/2_of_spades.png", face:"2",},
        {amount:1, imgLink:"images/PNG-cards-1.3/3_of_spades.png", face:"3",},
        {amount:1, imgLink:"images/PNG-cards-1.3/4_of_spades.png", face:"4",},
        {amount:1, imgLink:"images/PNG-cards-1.3/5_of_spades.png", face:"5",},
        {amount:1, imgLink:"images/PNG-cards-1.3/6_of_spades.png", face:"6",},
        {amount:1, imgLink:"images/PNG-cards-1.3/7_of_spades.png", face:"7",},
        {amount:1, imgLink:"images/PNG-cards-1.3/8_of_spades.png", face:"8",},
        {amount:1, imgLink:"images/PNG-cards-1.3/9_of_spades.png", face:"9",},
        {amount:1, imgLink:"images/PNG-cards-1.3/10_of_spades.png", face:"10",},
        {amount:1, imgLink:"images/PNG-cards-1.3/jack_of_spades2.png", face:"Jack",},
        {amount:1, imgLink:"images/PNG-cards-1.3/queen_of_spades2.png", face:"Queen",},
        {amount:1, imgLink:"images/PNG-cards-1.3/king_of_spades2.png", face:"King",},

        {amount:1, imgLink:"images/PNG-cards-1.3/ace_of_hearts.png", face:"Ace",},
        {amount:1, imgLink:"images/PNG-cards-1.3/2_of_hearts.png", face:"2",},
        {amount:1, imgLink:"images/PNG-cards-1.3/3_of_hearts.png", face:"3",},
        {amount:1, imgLink:"images/PNG-cards-1.3/4_of_hearts.png", face:"4",},
        {amount:1, imgLink:"images/PNG-cards-1.3/5_of_hearts.png", face:"5",},
        {amount:1, imgLink:"images/PNG-cards-1.3/6_of_hearts.png", face:"6",},
        {amount:1, imgLink:"images/PNG-cards-1.3/7_of_hearts.png", face:"7",},
        {amount:1, imgLink:"images/PNG-cards-1.3/8_of_hearts.png", face:"8",},
        {amount:1, imgLink:"images/PNG-cards-1.3/9_of_hearts.png", face:"9",},
        {amount:1, imgLink:"images/PNG-cards-1.3/10_of_hearts.png", face:"10",},
        {amount:1, imgLink:"images/PNG-cards-1.3/jack_of_hearts2.png", face:"Jack",},
        {amount:1, imgLink:"images/PNG-cards-1.3/queen_of_hearts2.png", face:"Queen",},
        {amount:1, imgLink:"images/PNG-cards-1.3/king_of_hearts2.png", face:"King",},

        {amount:1, imgLink:"images/PNG-cards-1.3/ace_of_clubs.png", face:"Ace",},
        {amount:1, imgLink:"images/PNG-cards-1.3/2_of_clubs.png", face:"2",},
        {amount:1, imgLink:"images/PNG-cards-1.3/3_of_clubs.png", face:"3",},
        {amount:1, imgLink:"images/PNG-cards-1.3/4_of_clubs.png", face:"4",},
        {amount:1, imgLink:"images/PNG-cards-1.3/5_of_clubs.png", face:"5",},
        {amount:1, imgLink:"images/PNG-cards-1.3/6_of_clubs.png", face:"6",},
        {amount:1, imgLink:"images/PNG-cards-1.3/7_of_clubs.png", face:"7",},
        {amount:1, imgLink:"images/PNG-cards-1.3/8_of_clubs.png", face:"8",},
        {amount:1, imgLink:"images/PNG-cards-1.3/9_of_clubs.png", face:"9",},
        {amount:1, imgLink:"images/PNG-cards-1.3/10_of_clubs.png", face:"10",},
        {amount:1, imgLink:"images/PNG-cards-1.3/jack_of_clubs2.png", face:"Jack",},
        {amount:1, imgLink:"images/PNG-cards-1.3/queen_of_clubs2.png", face:"Queen",},
        {amount:1, imgLink:"images/PNG-cards-1.3/king_of_clubs2.png", face:"King",},

        {amount:1, imgLink:"images/PNG-cards-1.3/ace_of_diamonds.png", face:"Ace",},
        {amount:1, imgLink:"images/PNG-cards-1.3/2_of_diamonds.png", face:"2",},
        {amount:1, imgLink:"images/PNG-cards-1.3/3_of_diamonds.png", face:"3",},
        {amount:1, imgLink:"images/PNG-cards-1.3/4_of_diamonds.png", face:"4",},
        {amount:1, imgLink:"images/PNG-cards-1.3/5_of_diamonds.png", face:"5",},
        {amount:1, imgLink:"images/PNG-cards-1.3/6_of_diamonds.png", face:"6",},
        {amount:1, imgLink:"images/PNG-cards-1.3/7_of_diamonds.png", face:"7",},
        {amount:1, imgLink:"images/PNG-cards-1.3/8_of_diamonds.png", face:"8",},
        {amount:1, imgLink:"images/PNG-cards-1.3/9_of_diamonds.png", face:"9",},
        {amount:1, imgLink:"images/PNG-cards-1.3/10_of_diamonds.png", face:"10",},
        {amount:1, imgLink:"images/PNG-cards-1.3/jack_of_diamonds2.png", face:"Jack",},
        {amount:1, imgLink:"images/PNG-cards-1.3/queen_of_diamonds2.png", face:"Queen",},
        {amount:1, imgLink:"images/PNG-cards-1.3/king_of_diamonds2.png", face:"King",},

    ];

    playerHand = []
    playerPoints = 0

    dealerHand = []
    dealerPoints = 0

    isStanding = false;
    deckMultiplier = 1;

    hasDealRun = false;

    clearDiv("player-hand");
    clearDiv("dealer-hand");
}

/**Returns a random number between 0 and max, excludes 0.
 * @param {Number} max      The highest number that can be returned.
 * 
 * @returns {Number}        Returns random number.
 */
function randomNumber(max) {

    return (Math.floor((Math.random()*max)));
}

/**Selects a random card from the deck.
 * @param {Array} deck      The Deck formulated as an array.
 * 
 * @returns {Object}        An object representing a card.
 */
function findRandomCard(deck) {

    let index = randomNumber(deck.length);
    while (deck[index].amount < 1) {
        index = randomNumber(deck.length);
    }

    deck[index].amount--
    return deck[index];
}

/**Creates an img element from a card object.
 * @param {object} card     An object representing a card.
 * 
 * @returns {Object}        An img element based on a card object.
 */
function createCard(card) {

    let newImg = document.createElement("img");

    newImg.setAttribute("class", "card");
    newImg.setAttribute("src", card.imgLink)
    return newImg;
}

/**Deletes all elements in a Div.
 * @deprecated 1.0.0 Unused.
 * 
 * @param {String} divId    ID of a div to clear.
 */
function clearDiv(divId) {

    let box = document.getElementById(divId)
    while (box.firstChild) {
        box.removeChild(box.firstChild)
    }
}

/**Appends elements to a Div.
 * 
 * @param {String} divId    Id of a div to append to.
 * @param {Object} element  An element to append.
 */
function drwToDiv(divId, element) {

    let box = document.getElementById(divId);
    box.appendChild(element)
}

/**Pushes card object to array.
 * 
 * @param {Array} hand      An array representing the player's hand to push to.
 * @param {Object} card     An object representing a card to push.
 */
function addToHand(hand, card) {
    hand.push(card);
}

/**Clears the player's hand.
 * @deprecated 1.0.0          Unused
 * 
 * @param {Array} hand      An array represent the player's hand.
 */
function clearHand(hand) {
    hand.length = 0;
}

/**Handle Aces.
 * 
 * @param {Number} points       The points of the player whose hand is being evaluated.
 * 
 * @returns {Number}            The value of the Ace card.
 */
function aceHandler(points) {
    if ((points + 11) > 21) {
        return 1;
    }
    return 11;
}

/**Find the score of a card
 * 
 * @param {Object} card         An object representing a card.
 * @param {Number} player       A number representing player points.
 * 
 * @returns {Number}            A number represent the point value of a card.
 */
function findScore(card, player) {
    let points = 0;
    switch(card.face) {
        case "Ace":
            points += aceHandler(player);
            break;
        case "Jack":
            points += 10;
            break;
        case "Queen":
            points += 10;
            break;
        case "King":
            points += 10;
            break;
        default:
            points += Number(card.face)
    }
        return points;
}

/**Finds the total point values in a players hand.
 * 
 * @param {Array} hand              An Array representing a player's hand.
 * @param {Number} playerPoints     A Number representing a player's points.
 * 
 * @returns {Number}                A number representing a hand's total points.
 */
function evaluateHand(hand, playerPoints) {
    let handTotal = 0;
    hand.forEach(element => {
        handTotal += findScore(element, playerPoints);
    });
    return handTotal;
}

/**Writes a value the respective points element.
 * 
 * @param {String} player       A string containing player of dealer.
 * @param {*} score             The value to be written.
 */
function writeScore(player, score) {
    let label = document.getElementById(player + "-points")
    label.textContent = score
}

/**Deals card to the players.
 * 
 */
function deal() {
    if (!hasDealRun) {
        let counter = 2;
        while (counter > 0) {
            addToHand(playerHand, findRandomCard(fiftyTwoDeck));
            addToHand(dealerHand, findRandomCard(fiftyTwoDeck));
            counter--;
        }
        writeScore("player", evaluateHand(playerHand, playerPoints));
        //writeScore("dealer", evaluateHand(dealerHand))

        playerPoints = evaluateHand(playerHand, playerPoints);
        dealerPoints = evaluateHand(dealerHand, dealerPoints);

        drwHandOnDeal();
        evalWins(isStanding);
        hasDealRun = true;
    }
}

/**Reveals a card whose face value is hidden.
 * 
 * @param {Object} element      An img element to reveal.
 */
function revealCard(element) {
    element.setAttribute("src", element.getAttribute("custom"));
    element.removeAttribute("id");
}


/**Draw all the cards in the players' hand. 
 * Also hide one card of the dealers. 
 * Meant to be fired exclusively in the deal phase.
 * 
 */
function drwHandOnDeal() {

    playerHand.forEach(element => {
        drwToDiv("player-hand", createCard(element));
    })

    dealerHand.forEach(element => {
        let newCardElement = createCard(element)
        newCardElement.setAttribute("custom", newCardElement.src)
        newCardElement.setAttribute("id", "hidden-card")
        newCardElement.src = "images/PNG-cards-1.3/back@2x.png"
        drwToDiv("dealer-hand", newCardElement)
    })

    let firstCard = document.getElementById("dealer-hand").firstElementChild
    revealCard(firstCard);


}

/**Add a new card to the player's(and not the dealers) hand.
 * 
 * @param {String} handStr      The ID of the div to draw to.
 * @param {Object} card         The card to draw.
 */
function drwHandOnHit(handStr, card) {
    drwToDiv(handStr, createCard(card))
}

/**This function runs when the player presses the hit button.
 * 
 */
function hit() {
    let newCard = findRandomCard(fiftyTwoDeck);
    addToHand(playerHand, newCard);
    drwHandOnHit("player-hand", newCard);
    writeScore("player", evaluateHand(playerHand, playerPoints));
    playerPoints = evaluateHand(playerHand, playerPoints);
    evalWins(isStanding);
}

/**This function runs when it's time for the dealer to hit.
 * 
 */
function dealerHit() {

    let newCard = findRandomCard(fiftyTwoDeck);

    addToHand(dealerHand, newCard);
    drwHandOnHit("dealer-hand", newCard);
    writeScore("dealer", evaluateHand(dealerHand, dealerPoints));
    dealerPoints = evaluateHand(dealerHand, dealerPoints)
    evalWins(isStanding)
}

/**Displays a win message
 * 
 * @param {Boolean} isWinner        Boolean indicating wether the player has won.
 * @param {Boolean} isBlackJack     Boolean indicating wether the player has a blackjack.
 */
function win(isWinner=true, isBlackJack=false) {
    //revealCard(document.getElementById("hidden-card"))
    let buttonDiv = document.getElementById("button-container")
    let div = document.getElementById("messages")
    if (isWinner && isBlackJack) {
        div.textContent = "BlackJack! You Won!";
    } else if (isWinner) {
        div.textContent = "You're a Winner!";
    } else {
        div.textContent = "You Lost!";
    }
    buttonDiv.innerHTML = "<a href='index.html'>Play Again";
    // buttonDiv.innerHTML = "<button id='play-again'>Play Again</button>'";
    // document.getElementById("play-again").addEventListener("click", setup)

}

/**Fired when the stand button is pressed
 * 
 */
function stand() {
    isStanding = true;
    dealerTurn(isStanding);
}

/**This function makes the dealer draw card until he has a score >17.
 * 
 * @param {Boolean} isStanding        Boolean indicating wether the player is standing.
 */
function dealerTurn(isStanding) {
    if (document.getElementById("hidden-card")) {
        revealCard(document.getElementById("hidden-card")) 
    }
    
    if (isStanding) {
        while (dealerPoints < 17) {
            dealerHit();
        }
    }
    evalWins(isStanding)
}


/**Checks if any win conditions have been met.
 * 
 * @param {Boolean} stand         Boolean indicating wether the player is standing.
 */
function evalWins(stand) {
    if (dealerPoints > 21) {
        win()
    } else if (dealerPoints == 21) {
        win(false)
    } else if (dealerPoints >= playerPoints && stand) {
        win(false)
    }

    if (playerPoints > 21) {
        win(false)
    } else if (playerPoints == 21) {
        win(true, true)
    } else if (playerPoints > dealerPoints && stand) {
        win()
    }
}

/**Changes the number of cards in the deck.
 * 
 */
function changeDeck() {
    let deck = fiftyTwoDeck;
    let div = document.getElementById("deck-type");
    if (deckMultiplier == 1) {
        deckMultiplier = 3;
        div.textContent = "3x Deck";
    } else if (deckMultiplier == 3) {
        deckMultiplier = 6;
        div.textContent = "6x Deck";
    } else {
        deckMultiplier = 1;
        div.textContent = "1x Deck";
    }
    deck.forEach(element => {
        element.amount = 1 * deckMultiplier;
    })

}

var fiftyTwoDeck;

var playerHand
var playerPoints

var dealerHand
var dealerPoints

var isStanding
var deckMultiplier

var hasDealRun

setup()

document.getElementById("deal-button").addEventListener("click", deal);
document.getElementById("hit-button").addEventListener("click", hit)
document.getElementById("stand-button").addEventListener("click", stand)
document.getElementById("change-deck").addEventListener("click", changeDeck)




// // drwToDiv("player-hand", createCard(findRandomCard(fiftyTwoDeck)))

// playerHand.push(findRandomCard(fiftyTwoDeck))
// writeScore("player", 50)
// evaluateHand(playerHand)
// console.log(playerHand)