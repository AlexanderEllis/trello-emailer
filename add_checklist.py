from trello import TrelloClient
from config import *

"""
This is a sample filler file that adds a checklist to a card.  It assumes the card already exists and
is the first card in the list of cards, and I will add the function for creating a card as well.

1-24 with Reading, Lecture, Recitation, and Tests is made from the MIT OCW Introduction to Algorithms class
to see how it would work.

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/


"""
trello = TrelloClient(TRELLO_API_INFO['api_key'], TRELLO_API_INFO['api_secret'], TRELLO_API_INFO['token'], TRELLO_API_INFO['token_secret'])

board = trello.get_board(BOARDS_TO_WATCH[0]) # Assuming the board you're targeting is the first in the list

cards = board.open_lists()[1].list_cards()

TODO = []

for i in range(1, 25):
    TODO.append('Reading ' + str(i))
    TODO.append('Lecture ' + str(i))
    TODO.append('Recitation ' + str(i))
    if i % 3 == 0:
        TODO.append('PSET ' + str(i / 3))
    if i % 12 == 0:
        TODO.append('TEST ' + str(i / 12))

cards[0].add_checklist('TODO', TODO) # Assuming the card you want to target is first in the list of cards
