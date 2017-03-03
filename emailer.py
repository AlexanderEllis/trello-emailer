from trello import TrelloClient
from config import * 
from send_email import send_email

trello = TrelloClient(TRELLO_API_INFO['api_key'], TRELLO_API_INFO['api_secret'], TRELLO_API_INFO['token'], TRELLO_API_INFO['token_secret']) 

email_body = []

def analyze_boards(board_array):
    for board in board_array:
        board_obj = trello.get_board(board)
        cards = board_obj.open_lists()[1].list_cards()
 
        for card in cards:
            email_body.append(card.name)
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
            email_body.append('  ' + each_list.name)
            for item in TODO:
                email_body.append('    ' + item)

analyze_boards(BOARDS_TO_WATCH)

send_email('\r\n'.join(email_body))
