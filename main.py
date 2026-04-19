"""  STUDENT PROFILE MANAGEMENT SYSTEM FODS Final Assessment Project """

import os


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