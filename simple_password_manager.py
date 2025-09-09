import json
import base64
import os

DATA_FILE = "passwords.json"


class PasswordManager:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Load existing password data from file"""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_data(self):
        """Save data to file"""
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def encode_password(self, password: str) -> str:
        """Encode password using Base64"""
        return base64.b64encode(password.encode("utf-8")).decode("utf-8")

    def decode_password(self, encoded: str) -> str:
        """Decode Base64 password"""
        return base64.b64decode(encoded.encode("utf-8")).decode("utf-8")

    def add_entry(self, website: str, username: str, password: str):
        """Add new entry"""
        encoded_pw = self.encode_password(password)
        entry = {
            "website": website,
            "username": username,
            "password": encoded_pw
        }
        self.data.append(entry)
        self.save_data()
        print(f"✅ Saved login for {website}")

    def list_entries(self):
        """List stored entries"""
        if not self.data:
            print("No saved logins yet.")
            return
        for i, entry in enumerate(self.data, start=1):
            print(f"{i}. {entry['website']} - {entry['username']}")

    def get_password(self, website: str):
        """Retrieve and decode password for given website"""
        for entry in self.data:
            if entry["website"].lower() == website.lower():
                decoded_pw = self.decode_password(entry["password"])
                print(f"🔑 {website} ({entry['username']}): {decoded_pw}")
                return
        print("❌ Website not found in database.")


def main():
    manager = PasswordManager()

    while True:
        print("\n--- Password Manager ---")
        print("1. Add new login")
        print("2. List saved logins")
        print("3. Get password for a website")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            website = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")
            manager.add_entry(website, username, password)

        elif choice == "2":
            manager.list_entries()

        elif choice == "3":
            site = input("Enter website name: ")
            manager.get_password(site)

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
