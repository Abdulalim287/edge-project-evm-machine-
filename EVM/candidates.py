import os

def manage_candidates():
    while True:
        print("\n========= CANDIDATE MANAGEMENT =========")
        print("1. Add Candidate")
        print("2. View All Candidates")
        print("3. Search Candidate by Name")
        print("4. Delete Candidate")
        print("5. Return to Admin Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_candidate()
        elif choice == "2":
            view_candidates()
        elif choice == "3":
            search_candidate()
        elif choice == "4":
            delete_candidate()
        elif choice == "5":
            break
        else:
            print("Invalid input! Please try again.")

def add_candidate():

    serial = 1
    if os.path.exists("data/candidates.txt"):
        with open("data/candidates.txt", "r") as file:
            lines = file.readlines()
            serial = len(lines) + 1

    name = input("Enter Candidate Name: ").upper()
    symbol = input("Enter Mark: ").upper()
    party = input("Enter Party: ").upper()


    record = f"SI_NO:{serial}  Candidate Name:{name}  Mark:{symbol}  Party:{party}\n"
    with open("data/candidates.txt", "a") as file:
        file.write(record)

    print("Candidate added successfully!")

def view_candidates():
    if not os.path.exists("data/candidates.txt"):
        print("No candidates available!")
        return

    with open("data/candidates.txt", "r") as file:
        candidates = file.readlines()
        if not candidates:
            print("No candidates available!")
            return
        print("\n===== Candidate List =====")
        for candidate in candidates:
            print(candidate.strip())

def search_candidate():
    name = input("Enter Candidate Name to Search: ").lower()
    found = False

    if not os.path.exists("data/candidates.txt"):
        print("No data found!")
        return

    with open("data/candidates.txt", "r") as file:
        for line in file:
            # Check if the candidate name (after the prefix) matches the search term.
            if name.lower() in line.lower():
                print(line.strip())
                found = True

    if not found:
        print("Candidate not found!")

def delete_candidate():
    name = input("Enter Candidate Name to Delete: ")

    if not os.path.exists("data/candidates.txt"):
        print("No data found!")
        return

    with open("data/candidates.txt", "r") as file:
        lines = file.readlines()

    with open("data/candidates.txt", "w") as file:
        deleted = False
        for line in lines:
            # If the line (ignoring case) contains the candidate name, remove it.
            if name.lower() in line.lower():
                deleted = True
                continue
            file.write(line)

    if deleted:
        print("Candidate deleted successfully!")
    else:
        print("Candidate not found!")
