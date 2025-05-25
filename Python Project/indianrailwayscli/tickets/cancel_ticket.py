from utils.data_io import load_json, write_json

def cancel_ticket(user):
    tickets = load_json("data/tickets.json")
    ticket_id = input("Enter ticket ID to cancel: ").strip()

    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id and ticket['user_id'] == user['id']:
            ticket['status'] = "Cancelled"
            write_json("data/tickets.json", tickets)
            print("Ticket cancelled successfully.")
            return

    print("Ticket not found or unauthorized access.")
