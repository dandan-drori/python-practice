import random

picture_cards = {
  'J': 11,
  'Q': 12,
  'K': 13,
}

class Deck:
  deck = []

  def __init__(self):
    self.make_deck()

  def make_deck(self):
    deck = []
    for i in range(1, 14):
      for j in range(4):
        if i == 11:
          deck.append('J')
        elif i == 12:
          deck.append('Q')
        elif i == 13:
          deck.append('K')
        else:
          deck.append(i)
    self.deck = deck

  def draw_card(self):
    card = random.choice(self.deck)
    self.deck.remove(card)
    return card

class Player:
  deck = {}
  cards = []

  def __init__(self, deck):
    self.deck = deck
    self.draw_cards(2)

  def draw_cards(self, quantity):
    for i in range(quantity):
      card = self.deck.draw_card()
      self.cards.append(card)
  
  def show_cards(self):
    print('Your Cards: ', end='')
    print(self.cards)

  def get_sum(self):
    count = 0
    for card in self.cards:
      if isinstance(card, int):
        count += card
      else:
        count += picture_cards[card]
    return count

  def is_lose(self):
    count = self.get_sum()
    if count > 21:
      return True

class Dealer(Player):
  def __init__(self, deck):
    self.deck = deck
    self.draw_cards(2)
    super().__init__(deck)

  def show_cards(self):
    if len(self.cards) == 2:
      print('Dealers Cards: ', end='')
      print(self.cards[0], end='')
      print(', ?]')
    else:
      print('Dealers Cards: ', end='')
      print(self.cards)

def end_game(winner, dealer, player):
  print('Game Over')
  print('Winner: ' + winner)
  print('Dealer count: ' + str(dealer.get_sum()))
  print('Your count: ' + str(player.get_sum()))
  return False

def main():
  game_over = False
  deck = Deck()
  dealer = Dealer(deck)
  player = Player(deck)
  dealer.show_cards()
  player.show_cards()
  while not game_over:
    draw = input('Draw a card? Y/N ').upper()
    if draw == 'Y':
      player.draw_cards(1)
      if player.is_lose():
        game_over = end_game('Dealer', dealer, player)
      dealer.draw_cards(1)
      if dealer.is_lose():
        game_over = end_game('Player', dealer, player)
    else:
      dealer.draw_cards(1)

main()
