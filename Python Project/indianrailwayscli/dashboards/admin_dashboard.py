from admin.train_management import train_management_menu
from admin.timetable_management import manage_timetables

def admin_dashboard(user):
    while True:
        print(f"\nAdmin Dashboard — Welcome {user['username']}")
        print("1. Manage Trains")
        print("2. Timetable & Stop Management")
        print("3. Manage Users")
        print("4. View Reports")
        print("5. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            train_management_menu()
        elif choice == "2":
            manage_timetables()
        elif choice == "3":
            print("User management coming soon...")
        elif choice == "4":
            print("Reports module coming soon...")
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")
