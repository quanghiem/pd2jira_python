from Ticket import Ticket
from PagerDuty import PagerDuty


def lambda_handler(event, context):
    main(event, is_lambda=True)

def main(event, is_lambda=True):
    messages = event['messages']
    for message in messages:
        message_data = message['data']
        if PagerDuty.is_triggered_alert(message_data) and not Ticket.exists(message_data):
            ticket = Ticket(message_data, is_lambda)
            ticket.create()
            # TODO update_pager_duty_with_ticket_info()

if __name__ == '__main__':
    event = argv[1]
    main(event, is_lambda=False)
