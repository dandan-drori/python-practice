import random

picture_cards = {
  'J': 10,
  'Q': 10,
  'K': 10,
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
  deck = {}
  cards = []

  def __init__(self, deck):
    self.deck = deck
    self.draw_cards(2)

  def show_cards(self):
    if len(self.cards) == 2:
      print('Dealers Cards: ', end='')
      print(self.cards[0], end='')
      print(', ?]')
    else:
      print('Dealers Cards: ', end='')
      print(self.cards)

def end_game(winner, dealer, player):
  dealer_count = dealer.get_sum()
  player_count = player.get_sum()
  is_win = False
  if dealer_count > player_count and dealer_count <= 21:
    winner = 'Dealer'
    is_win = True
  elif player_count > dealer_count and player_count <= 21:
    winner = 'Player'
    is_win = True
  if dealer.is_lose():
    winner = 'Player'
    is_win = True
  elif player.is_lose():
    winner = 'Dealer'
    is_win = True
  if is_win:
    print('Game Over')
    print('Winner: ' + winner)
    print('Dealer count: ' + str(dealer_count))
    print('Your count: ' + str(player_count))
  return is_win

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
      dealer.show_cards()
      player.show_cards()
    else:
      dealer.draw_cards(1)
      game_over = end_game('Player', dealer, player)
      print(game_over)
      if game_over:
        return
      while not dealer.is_lose() and player.get_sum() > dealer.get_sum() and not player.is_lose():
        game_over = end_game('Player', dealer, player)
        if not game_over:
          dealer.draw_cards(1)
      dealer.show_cards()
      player.show_cards()

main()
