def staff_dashboard(user):
    while True:
        print(f"\nStaff Dashboard — Hello {user['username']}")
        print("1. View Assigned Duties")
        print("2. Update Train Status")
        print("3. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Assigned duties coming soon...")
        elif choice == "2":
            print("Train status update coming soon...")
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")
