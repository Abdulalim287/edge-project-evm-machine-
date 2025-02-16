import candidates
import voters
import results

def admin_panel():
    while True:
        print("\n=========== ADMIN PANEL ===========")
        print("1. Manage Candidates")
        print("2. Manage Voters")
        print("3. View Election Results")
        print("4. Return to Main Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            candidates.manage_candidates()
        elif choice == "2":
            voters.manage_voters()
        elif choice == "3":
            results.results_menu()
        elif choice == "4":
            break
        else:
            print("Invalid input! Please try again.")
