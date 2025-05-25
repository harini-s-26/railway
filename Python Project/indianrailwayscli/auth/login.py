from utils.data_io import load_json

def login_user():
    users = load_json("data/users.json")

    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Login successful. Welcome, {user['username']}!")
            return user

    print("Invalid email or password.")
    return None
