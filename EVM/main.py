import voting
import admin

def main_menu():
    while True:
        print("\n===== EVM Machine =====")
        print("1. Cast Vote")

        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            voting.cast_vote()
        elif choice == "admin":
            password = input("Enter Admin Password: ")
            if password == "admin123":
                admin.admin_panel()
            else:
                print("Incorrect password! Access denied.")
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    main_menu()
