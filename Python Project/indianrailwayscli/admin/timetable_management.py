import uuid
from utils.data_io import load_json, write_json

def manage_timetables():
    while True:
        print("\nTimetable & Stop Management")
        print("1. Add Timetable")
        print("2. View Timetables")
        print("3. Delete Timetable")
        print("4. Go Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_timetable()
        elif choice == "2":
            view_timetables()
        elif choice == "3":
            delete_timetable()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def add_timetable():
    timetables = load_json("data/timetables.json")

    train_id = input("Enter Train ID to assign timetable: ").strip()
    stops = []

    while True:
        station = input("Enter station name (or 'done' to finish): ").strip()
        if station.lower() == 'done':
            break
        arrival = input(f"Arrival time at {station} (HH:MM): ").strip()
        departure = input(f"Departure time at {station} (HH:MM): ").strip()
        platform = input(f"Platform number at {station}: ").strip()
        stops.append({
            "station": station,
            "arrival": arrival,
            "departure": departure,
            "platform": platform
        })

    timetable = {
        "id": str(uuid.uuid4()),
        "train_id": train_id,
        "stops": stops
    }

    timetables.append(timetable)
    write_json("data/timetables.json", timetables)
    print("Timetable added successfully.")

def view_timetables():
    timetables = load_json("data/timetables.json")
    if not timetables:
        print("No timetables available.")
        return

    for t in timetables:
        print(f"\n🆔 Timetable ID: {t['id']} | Train ID: {t['train_id']}")
        for stop in t['stops']:
            print(f"  • {stop['station']} | Arr: {stop['arrival']} | Dep: {stop['departure']} | Platform: {stop['platform']}")

def delete_timetable():
    timetables = load_json("data/timetables.json")
    tid = input("Enter Timetable ID to delete: ").strip()
    new_list = [t for t in timetables if t['id'] != tid]
    
    if len(new_list) == len(timetables):
        print("Timetable ID not found.")
    else:
        write_json("data/timetables.json", new_list)
        print("Timetable deleted.")
