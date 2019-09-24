
var fiftyTwoDeck = [
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

var playerHand = []
var playerPoints = 0

var dealerHand = []
var dealerPoints = 0

function randomNumber(max) {
    /**Returns a random number between 0 and max, excludes 0.
     * @param:      {number} max The highest number that can be returned.
     * 
     * @returns:    {number} Returns random number.
     */
    return (Math.floor((Math.random()*max)));
}

function findRandomCard(deck) {
    let index = randomNumber(deck.length);
    while (deck[index].amount < 1) {
        index = randomNumber(deck.length);
    }

    return deck[index];
}

function createCard(card) {
    let newImg = document.createElement("img");

    newImg.setAttribute("class", "card");
    newImg.setAttribute("src", card.imgLink)
    return newImg;
}

function drwToDiv(divId, element) {
    let box = document.getElementById(divId);
    box.appendChild(element)
}

function addToHand(hand, card) {
    hand.push(card);
}

function clearHand(hand) {
    hand.length = 0;
}

function aceHandler() {
return 1;
}

function findScore(card) {
    let points = 0;
    switch(card.face) {
        case "Ace":
            points += aceHandler();
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

function evaluateHand(hand) {
    let handTotal = 0;
    hand.forEach(element => {
        handTotal += findScore(element);
    });
    return handTotal;
}

function writeScore(player, score) {
    let label = document.getElementById(player + "-points")
    label.textContent = score
}

function deal() {
    let counter = 2
    while (counter > 0) {
        addToHand(playerHand, findRandomCard(fiftyTwoDeck))
        addToHand(dealerHand, findRandomCard(fiftyTwoDeck))
        counter--;
    }
    writeScore("player", evaluateHand(playerHand))
    writeScore("dealer", evaluateHand(dealerHand))

    drwHand()
    
}

function drwHand() {
    playerHand.forEach(element => {
        drwToDiv("player-hand", createCard(element))
    })

    dealerHand.forEach(element => {
        drwToDiv("dealer-hand", createCard(element))
    })
}

function main() {

}

document.getElementById("deal-button").addEventListener("click", deal);





// // drwToDiv("player-hand", createCard(findRandomCard(fiftyTwoDeck)))

// playerHand.push(findRandomCard(fiftyTwoDeck))
// writeScore("player", 50)
// evaluateHand(playerHand)
// console.log(playerHand)