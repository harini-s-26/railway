import uuid
from utils.data_io import load_json, write_json

def book_ticket(user):
    trains = load_json("data/trains.json")
    tickets = load_json("data/tickets.json")

    source = input("Enter source station: ").strip().lower()
    destination = input("Enter destination station: ").strip().lower()

    # Filter trains that match source and destination exactly
    available_trains = [
        train for train in trains
        if train['source'].lower() == source and train['destination'].lower() == destination
    ]

    if not available_trains:
        print("No trains available between these stations.")
        return

    print("\nAvailable Trains:")
    for idx, train in enumerate(available_trains, 1):
        print(f"{idx}. {train['train_name']} ({train['train_number']})")

    try:
        tno = int(input("Select train number to book: ").strip()) - 1
        if tno < 0 or tno >= len(available_trains):
            raise ValueError
    except ValueError:
        print(" Invalid train selection.")
        return

    selected_train = available_trains[tno]
    passenger_name = input("Enter passenger name: ").strip()
    age = input("Enter age: ").strip()
    gender = input("Enter gender: ").strip()

    ticket = {
        "ticket_id": str(uuid.uuid4()),
        "user_id": user['id'],
        "train_number": selected_train['train_number'],
        "train_name": selected_train['train_name'],
        "passenger_name": passenger_name,
        "age": age,
        "gender": gender,
        "source": source,
        "destination": destination,
        "status": "Confirmed"
    }

    tickets.append(ticket)
    write_json("data/tickets.json", tickets)
    print(f"Ticket booked successfully. Ticket ID: {ticket['ticket_id']}")