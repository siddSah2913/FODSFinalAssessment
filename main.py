"""  STUDENT PROFILE MANAGEMENT SYSTEM FODS Final Assessment Project """

import os

# Files setup function
def setup_files():
    """Creating the 4 data files with sample data if they don't already exist."""

    if not os.path.exists("users.txt"):
        # File containing user information
        with open("users.txt", "w") as f:
            f.write("admin01,Admin User,admin\n")
            f.write("s001,Siddhu Sah,student\n")
            f.write("s002,Yugant Adhikari,student\n")

    if not os.path.exists("passwords.txt"):
        # File containing password information
        with open("passwords.txt", "w") as f:
            f.write("admin01,admin123\n")
            f.write("s001,pass1234\n")
            f.write("s002,pass5678\n")

    if not os.path.exists("grades.txt"):
        with open("grades.txt", "w") as f:
            # Format: student_id, Math, CS, English, Science, Nepali
            f.write("s001,85,90,78,92,88\n")
            f.write("s002,72,65,80,70,75\n")

    if not os.path.exists("eca.txt"):
        with open("eca.txt", "w") as f:
            # Format: student_id, activity1, activity2 ...
            f.write("s001,Football,Music Club\n")
            f.write("s002,Dance,Debate Club,Art\n")

# Read file function
def read_file(filename):
    """Read all lines from a file and return as a list."""
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"  [!] File '{filename}' not found. Creating it now...")
        open(filename, "w").close()
        return []
    except Exception as e:
        print(f"  [!] Error reading '{filename}': {e}")
        return []

# Write file function
def write_file(filename, lines):
    """Write a list of lines back to a file."""
    try:
        with open(filename, "w") as f:
            for line in lines:
                f.write(line + "\n")
    except Exception as e:
        print(f"  [!] Error writing to '{filename}': {e}")

# Divider function (just for decoration)
def divider():
    print("\n" + "-" * 45 + "\n")

class User:
    """
    Base class is for all users.
    Both Admin and Student inherit from this.
    """

    # Constructor
    def __init__(self, user_id, name, role):
        self.user_id = user_id   
        self.name    = name      
        self.role    = role

    # Show profile function
    def show_profile(self):
        """Print this user's basic profile."""
        print(f"\n  Name    : {self.name}")
        print(f"  ID      : {self.user_id}")
        print(f"  Role    : {self.role.capitalize()}")
    
    # Update profile function
    def update_profile(self):
        """Let a user change their own name."""
        try:
            print(f"\n  Current name: {self.name}")
            new_name = input("  Enter new name (or press Enter to keep): ").strip()
            if new_name:
                lines = read_file("users.txt")
                updated = []
                for line in lines:
                    parts = line.split(",")
                    if parts[0] == self.user_id:
                        parts[1] = new_name
                        self.name = new_name
                    updated.append(",".join(parts))
                write_file("users.txt", updated)
                print(f"  Name updated to '{new_name}'")
            else:
                print("  No changes made.")
        except Exception as e:
            print(f"  [!] Could not update profile: {e}")

# Main function
def main():
    setup_files()

    print("\n" + "=" * 45)
    print("   STUDENT PROFILE MANAGEMENT SYSTEM")
    print("   FODS Final Assessment 2026  ")
    print("=" * 45)
    
    # Maximum number of attempts
    MAX_ATTEMPTS = 3

    while True:
        attempts = 0
        user     = None

        while attempts < MAX_ATTEMPTS:
            user = login()
            if user:
                break
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"  {remaining} attempt(s) remaining.")

        if not user:
            print("\n  Too many failed attempts. Exiting for security.\n")
            break

        print(f"\n  Welcome, {user.name}!")

        if isinstance(user, Admin):
            user.admin_menu()
        else:
            user.student_menu()

        again = input("\n  Login as another user? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n  Thank you for using the system. Goodbye!\n")
            break


# Run the main function
if __name__ == "__main__":
    main()