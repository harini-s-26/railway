from utils.data_io import load_json

def view_bookings(user):
    tickets = load_json("data/tickets.json")
    user_tickets = [t for t in tickets if t['user_id'] == user['id']]

    if not user_tickets:
        print("ℹNo bookings found.")
        return

    print("\nYour Bookings:")
    for t in user_tickets:
        print(f"- Ticket ID: {t['ticket_id']}, {t['passenger_name']} from {t['source']} to {t['destination']} [{t['status']}]")
