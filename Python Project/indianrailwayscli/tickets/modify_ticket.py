from utils.data_io import load_json, write_json

def modify_ticket(user):
    tickets = load_json("data/tickets.json")
    ticket_id = input("Enter ticket ID to modify: ").strip()

    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id and ticket['user_id'] == user['id']:
            print("Enter new details (leave blank to keep existing):")
            new_name = input(f"Passenger Name [{ticket['passenger_name']}]: ").strip()
            new_age = input(f"Age [{ticket['age']}]: ").strip()

            if new_name:
                ticket['passenger_name'] = new_name
            if new_age:
                ticket['age'] = new_age

            write_json("data/tickets.json", tickets)
            print("Ticket updated successfully.")
            return

    print("Ticket not found or unauthorized access.")
