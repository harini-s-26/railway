from auth.register import register_user, login_user, remove_user
from dashboards.admin_dashboard import admin_dashboard
from dashboards.passenger_dashboard import passenger_dashboard
from dashboards.staff_dashboard import staff_dashboard

def main():
    while True:
        print("\nIndian Railways CLI System\n")
        print("1. Register")
        print("2. Login")
        print("3. Remove User (Admin only)")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            user = login_user()
            if user:
                if user["role"] == "admin":
                    admin_dashboard(user)
                elif user["role"] == "passenger":
                    passenger_dashboard(user)
                elif user["role"] == "staff":
                    staff_dashboard(user)
                else:
                    print("Unknown role. Contact system admin.")
        elif choice == "3":
            remove_user()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
