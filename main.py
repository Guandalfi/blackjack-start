import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Função para adicionar uma nova carta a mão do jogador
def deal_card(hand, score):
  card = cards[random.randint(0, 12)]
  if card == 11:
    if score > 11:
      hand.append(card - 10)
    else:
        hand.append(card)
  else:
    hand.append(card)

def random_start_hand():
  return cards[random.randint(0, 12)], cards[random.randint(0, 12)]

def count_player_score(cards):
  score = 0
  for card in cards:
    score += card
  return score
  
def count_computer_score(cards):
  score = 0
  for card in cards:
    score += card
  return score
def winner(score_player, score_computer):
  winner = ''
  if score_player > score_computer:
    winner = 'player'
    return winner
  elif score_computer > score_player and score_computer < 22:
    winner = 'computer'
    return winner
  elif score_computer > 21:
    winner = 'player'
    return winner
  else:
    return 'draw'


start_the_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
playing_the_game = True
def start_game():
    clear()
    print(logo)
    playing_the_game = True
    #Mão inicial do jogador
    player_cards = list(random_start_hand())
    #mão inicial do computador
    computer_cards = list(random_start_hand())
    #Verifica a soma das cartas
    player_score = count_player_score(player_cards)
    computer_score = count_computer_score(computer_cards)
    

    print(f"   your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    #Verifica se o jogador fez 21 na mão inicial
    if player_score == 21:
        clear()
        print(logo)
        print(f"   Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {computer_cards}, final score {computer_score}")
        print("   You made 21, you win !!!")
        playing_the_game = False
        start_the_game = input("type 'y' to play again: ")
        if start_the_game == 'y':
          start_game()
        else:
          playing_the_game = False
    
    while playing_the_game == True:
        #Verifica se o jogador quer comprar uma carta  
        wanna_draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if wanna_draw == 'y':
            deal_card(player_cards, player_score)
            #soma dos pontos do jogador
            player_score = count_player_score(player_cards)
            
            #Verifica se a pontuação é 21 apos comprar uma carta e ganha o jogo
            if player_score == 21:
                clear()
                print(logo)
                print(f"   Your final hand: {player_cards}, final score: {player_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("   you made 21, you win !!!")
                playing_the_game = False
          
        #Verifica se o jogador passou de 21 e perde o jogo
            elif player_score > 21:
                clear()
                print(logo)
                print(f"   Your final hand: {player_cards}, final score {player_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("   You'r above 21, you lose !!!")
                playing_the_game = False
            elif player_score < 21:
                clear()
                print(logo)
                print(f"   your cards: {player_cards}, current score: {player_score}")
                print(f"Computer's first card: {computer_cards[0]}")
          
        elif wanna_draw == 'n':
            clear()
            print(logo)
            player_score = count_player_score(player_cards)
            print(f"   Your final hand: {player_cards}, your final score {player_score}")
      
            while computer_score < 17:
                deal_card(computer_cards, computer_score)
                computer_score = count_computer_score(computer_cards)
        
            print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
            game_winner = winner(player_score, computer_score)
        
            print(f"   The winner is the: {game_winner} !!!")
            start_the_game = input("type 'y' to play again: ")
            if start_the_game == 'y':
              start_game()
            else:
              playing_the_game = False
              
if start_the_game == 'y':
  start_game()
        
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
