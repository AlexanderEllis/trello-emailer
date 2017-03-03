from trello import TrelloClient
from config import * 


trello = TrelloClient(TRELLO_API_INFO['api_key'], TRELLO_API_INFO['api_secret'], TRELLO_API_INFO['token'], TRELLO_API_INFO['token_secret']) 

def analyze_boards(board_array):
    for board in board_array:
        board_obj = trello.get_board(board)
        cards = board_obj.open_lists()[1].list_cards()
 
        for card in cards:
            print(card.name)
            print_card_TODOs(card.fetch_checklists())

def print_card_TODOs(board):
    for each_list in board:
        incomplete = False
        TODO = []
        for item in each_list.items:
            if item['state'] == 'incomplete':
                incomplete = True
                TODO.append(item['name'])
                break
        if incomplete:
            print('  ' + each_list.name)
            for item in TODO:
                print('    ' + item)

analyze_boards(BOARDS_TO_WATCH)
