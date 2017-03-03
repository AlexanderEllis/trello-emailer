from trello import TrelloClient
from user_config import TRELLO_API_INFO, BOARDS_TO_WATCH
from send_email import send_email

def analyze_boards(board_list, trello_client, email_body):
    """
    This function takes in a list of Trello boards to anaylze
    For each card in each board, it parses for the checklists and adds them
    to the email using print_card_todos
    """
    for board in board_list:
        board_obj = trello_client.get_board(board)
        cards = board_obj.open_lists()[1].list_cards()
        # This is where I assume the 2nd card is "In Progress" and the one I want to analyze

        for card in cards:
            email_body.append(card.name)
            print_card_todos(card.fetch_checklists(), email_body)

def print_card_todos(checklists, email_body):
    """
    This function analyzes each checklist and adds the first incomplete item to the body of the
    email with indentation.
    """
    for checklist in checklists:
        incomplete = False
        todo = []
        for item in checklist.items:
            if item['state'] == 'incomplete':
                incomplete = True
                todo.append(item['name'])
                break
        if incomplete:
            email_body.append('  ' + checklist.name)
            for item in todo:
                email_body.append('    ' + item)

def emailer():
    """
    This function creates the Trello object, analyzes the boards, builds the email,
    and sends the email.
    """
    trello = TrelloClient(TRELLO_API_INFO['api_key'],
                          TRELLO_API_INFO['api_secret'],
                          TRELLO_API_INFO['token'],
                          TRELLO_API_INFO['token_secret'])

    email_body = []

    analyze_boards(BOARDS_TO_WATCH, trello, email_body)

    send_email('\r\n'.join(email_body))

if __name__ == '__main__':
    emailer()
