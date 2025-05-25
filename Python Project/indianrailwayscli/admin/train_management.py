import uuid
from utils.data_io import load_json, write_json

TRAIN_DATA_FILE = "data/trains.json"

def load_trains():
    return load_json(TRAIN_DATA_FILE)

def save_trains(trains):
    write_json(TRAIN_DATA_FILE, trains)

def add_train():
    trains = load_trains()
    train_name = input("Enter train name: ").strip()
    train_number = input("Enter train number: ").strip()
    source = input("Enter source station: ").strip()
    destination = input("Enter destination station: ").strip()
    frequency = input("Enter frequency (daily/weekly/monthly): ").strip()

    new_train = {
        "id": str(uuid.uuid4()),
        "train_name": train_name,
        "train_number": train_number,
        "source": source,
        "destination": destination,
        "frequency": frequency
    }

    trains.append(new_train)
    save_trains(trains)
    print("\nTrain added successfully.")

def view_trains():
    trains = load_trains()
    if not trains:
        print("\nNo trains available.")
        return
    print("\nAvailable Trains:")
    for idx, train in enumerate(trains, 1):
        print(f"{idx}. {train['train_number']} - {train['train_name']} ({train['source']} ➡ {train['destination']}) [{train['frequency']}]")

def delete_train():
    trains = load_trains()
    view_trains()
    try:
        idx = int(input("Enter train index to delete: ")) - 1
        if 0 <= idx < len(trains):
            deleted = trains.pop(idx)
            save_trains(trains)
            print(f"\nDeleted train: {deleted['train_name']}")
        else:
            print("\nInvalid index.")
    except ValueError:
        print("\nPlease enter a valid number.")

def train_management_menu():
    while True:
        print("\nTrain Management")
        print("1. Add Train")
        print("2. View Trains")
        print("3. Delete Train")
        print("4. Back to Admin Dashboard")
        choice = input("Enter choice: ").strip()

        if choice == '1':
            add_train()
        elif choice == '2':
            view_trains()
        elif choice == '3':
            delete_train()
        elif choice == '4':
            break
        else:
            print("\nInvalid option.")
