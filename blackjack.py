import random

class Deck(object):
  
  suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
  ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
  
  
  def __init__(self):
    self.listOfCards = []
    
  def listCards(self):
    for suit in self.suits:
      for rank in self.ranks:
        fullname = rank + " of " + suit
        #return rank + suit
        #print (rank + " of " + suit)
        self.listOfCards.append(fullname)
    #print (Deck.listOfCards)
    return self.listOfCards
  
  
  
    
class Hand(object):
  valueDictionary = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "1":10, "J":10, "Q":10, "K":10}
  
  def __init__(self, deck):
    self.deck = deck.listOfCards
    self.dealHand()
  
  def dealHand(self):  
    #print(len(self.deck))
    self.firstCard = random.choice(self.deck)
    self.deck.remove(self.firstCard)
    self.secondCard = random.choice(self.deck)
    self.deck.remove(self.secondCard)
    print (self.firstCard + " and " + self.secondCard)
    self.totalPoints = 0
    self.totalPoints = self.sumOfHand(self.firstCard, self.secondCard, self.totalPoints)
    self.decideIfBlackjack()
  
  def sumOfHand(self, card1, card2, score):
    self.card1 = card1
    self.card2 = card2
    self.score = score
    firstValue = self.valueDictionary[self.card1[0]]
    secondValue = self.valueDictionary[self.card2[0]]
    self.score = firstValue + secondValue
    #print (self.totalPoints)
    if firstValue == "A" and self.score > 10:
      self.score -= 10
    elif secondValue == "A" and self.score > 10:
      self.score -= 10
    print (self.score)
    print("------------------------------")
    return self.score
    
  def decideIfBlackjack(self):
    self.natural = False
    if self.totalPoints == 21:
      print ("Blackjack!")
      self.natural = True
      self.dealerHand()
      self.determineBlackjack()
    else:
      print ("Not blackjack yet")
      self.gamePlay()
      
  def gamePlay(self):
    if self.totalPoints < 21:
      answer = input("Hit or Stand? (H or S)")
      if answer == "h" or answer == "H":
        print ("..............................hitting")
        self.hit()
      elif answer == "s" or answer == "S":
        print("...............................standing")
        self.stand()
      else:
        print("Please choose a valid answer")
        self.gamePlay()
    elif self.totalPoints == 21:
      print("Blackjack!!!")
      self.dealerHand()
      self.determineBlackjack()
    else:
      print ("You lose this round.")
  
  def hit(self):
    self.newValue = 0
    self.newCard = random.choice(self.deck)
    self.deck.remove(self.newCard)
    print(self.newCard)
    self.newValue = self.valueDictionary[self.newCard[0]]
    if self.newValue == "A" and self.score > 10:
      self.score -= 10
    self.totalPoints += self.newValue
    print(self.totalPoints)
    self.gamePlay()
    
  def stand(self):
    self.dealerHand()
    
  def dealerHand(self):  
    self.dealerPoints = 0
    self.firstDealerCard = random.choice(self.deck)
    self.deck.remove(self.firstDealerCard)
    self.secondDealerCard = random.choice(self.deck)
    self.deck.remove(self.secondDealerCard)
    print(self.firstDealerCard + " and " + self.secondDealerCard)
    self.dealerPoints = self.sumOfHand(self.firstDealerCard, self.secondDealerCard, self.dealerPoints)
    
    if self.dealerPoints < 21 and self.natural == True:
      print("You win with a natural!")
    elif self.dealerPoints < 21:
      self.dealerTurn()
    else:
      print("Dealer wins, you lose.")
    
  def dealerTurn(self):
    if self.dealerPoints < 17:
      self.newDealerCard = random.choice(self.deck)
      self.deck.remove(self.newDealerCard)
      print(self.newDealerCard)
      self.newDealerValue = self.valueDictionary[self.newDealerCard[0]]
      self.dealerPoints += self.newDealerValue
      print(self.dealerPoints)
      self.dealerTurn()
    else:
      self.compareScores()
      
  def compareScores(self):
    if 22 > self.dealerPoints > self.totalPoints:
      print("You lose. The dealer wins.")
    elif self.dealerPoints < self.totalPoints:
      print("Congrats you win!")
    elif self.dealerPoints > 21:
      print("Dealer loses. You win!")
    else:
      print("It's a tie.")
      
  def determineBlackjack(self):
    if self.dealerPoints == 21:
      print("It's a tie.")
    else:
      print("With a perfect 21!")

  def playAgain(self):
    nextRound = input("Next round? (Y or N)")
    if nextRound == "Y" or nextRound == "y":
      self.dealHand()
    elif nextRound == "N" or nextRound == "n":
      print("Okay, later!")
    else:
      print("That wasn't valid input, try again.")
      self.playAgain()

 

firstDeck = Deck()
firstDeck.listCards()


hand1 = Hand(firstDeck)

while (len(firstDeck.listOfCards)) > 6:
  print("------------------------------")
  hand1.playAgain()



