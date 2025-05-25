import uuid
from utils.data_io import load_json, write_json

def register_user():
    users = load_json("data/users.json")

    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()
    role = input("Enter role (admin/passenger/staff): ").strip().lower()

    for user in users:
        if user["email"].lower() == email.lower():
            print("User already exists with this email.")
            return

    new_user = {
        "id": str(uuid.uuid4()),
        "username": username,
        "email": email,
        "password": password,  
        "role": role
    }

    users.append(new_user)
    write_json("data/users.json", users)
    print("Registration successful.")

def login_user():
    users = load_json("data/users.json")

    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    for user in users:
        if user["email"].lower() == email.lower() and user["password"] == password:
            print(f"Login successful. Welcome, {user['username']} ({user['role']})!")
            return user  
    print("Invalid email or password.")
    return None

def remove_user():
    users = load_json("data/users.json")
    email_to_remove = input("Enter email of user to remove: ").strip()

    updated_users = [user for user in users if user["email"].lower() != email_to_remove.lower()]

    if len(updated_users) == len(users):
        print(f"No user found with email: {email_to_remove}")
        return

    write_json("data/users.json", updated_users)
    print(f"User with email {email_to_remove} removed successfully.")
