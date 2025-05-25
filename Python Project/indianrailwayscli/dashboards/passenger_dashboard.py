from tickets.booking import book_ticket
from tickets.view_bookings import view_bookings
from tickets.cancel_ticket import cancel_ticket
from tickets.modify_ticket import modify_ticket  

def passenger_dashboard(user):
    while True:
        print(f"\nPassenger Dashboard — Hello {user['username']}")
        print("1. Book Ticket")
        print("2. View My Bookings")
        print("3. Cancel Ticket")
        print("4. Modify Ticket")
        print("5. Feedback")
        print("6. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_ticket(user)
        elif choice == "2":
            view_bookings(user)
        elif choice == "3":
            cancel_ticket(user)
        elif choice == "4":
            modify_ticket(user)
        elif choice == "5":
            print("Feedback module coming soon...")
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")
