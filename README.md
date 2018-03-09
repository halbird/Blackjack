# Blackjack
Game of Blackjack written in python.  

Use Deck object and Hand object to keep track of which cards have been used from the deck and which cards are currently in the hand. Build standard deck of cards. Set the values of the cards when dealt in a hand, Ace can be 1 or 11 points to best aim for 21 total. Deal a random hand (2 cards from the deck). Add up the points of the hand and determine if less than, equal to, or greater than 21 (blackjack). If 21, game ends and player wins, asked to play again. If less than 21, player asked to hit (add random card from deck to hand) or stand (end turn with current hand value). Score is re-evaluated, player can continue to hi as long as score is less than 21. If player stands, dealer's hand is dealt. If the value of the dealer's cards are less than 17, they are forced to receive another card. Score is added and compared to player's score. If dealer score is greater than 17, greater than player score, and less than or equal to 21, the dealer wins and the player loses. If the dealer score goes over 21, the player wins. Option to play next round until the deck has been used up.   

To-dos:
* Add additional gameplay options, there are more complicated rules to Blackjack that have not been incorporated
* Add option for multiple decks
* Add option for multiple players
* Keep track of scores/stats over time
* Graphics

