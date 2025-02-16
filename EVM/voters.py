import os


def manage_voters():
    while True:
        print("\n===== Voter Management =====")
        print("1. Add Voter")
        print("2. View All Voters")
        print("3. Search Voter by Name")
        print("4. Delete Voter")
        print("5. Return to Admin Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_voter()
        elif choice == "2":
            view_voters()
        elif choice == "3":
            search_voter()
        elif choice == "4":
            delete_voter()
        elif choice == "5":
            break
        else:
            print("Invalid input! Please try again.")


def is_unique_voter_id(voter_id):
    """Check if the voter ID already exists"""
    if not os.path.exists("data/voters.txt"):
        return True

    with open("data/voters.txt", "r") as file:
        for line in file:
            existing_id = line.strip().split(" ")[0]
            if existing_id == voter_id:
                return False
    return True


def add_voter():
    """Add a new voter with a unique ID"""
    voter_id = input("Enter Voter ID: ").strip()

    # Ensure ID is unique
    if not is_unique_voter_id(voter_id):
        print("This Voter ID is already registered! Try again.")
        return

    name = input("Enter Voter Name: ").strip()

    try:
        day, month, year =map( int,input("Enter Birth Day (DD MM YYYY): ").split())
         # = int(input("Enter Birth Month (integer): "))
         # = int(input("Enter Birth Year (integer): "))
    except ValueError:
        print("Birth day, month, and year must be integers.")
        return

    # Save the record in space-separated format: ID Name Day Month Year
    record = f"ID: {voter_id}   Name: {name}   Birth-date: {day} {month} {year}\n"

    with open("data/voters.txt", "a") as file:
        file.write(record)

    print("Voter added successfully!")


def view_voters():
    """View all registered voters"""
    if not os.path.exists("data/voters.txt"):
        print("No voters available!")
        return

    with open("data/voters.txt", "r") as file:
        voters = file.readlines()
        if not voters:
            print("No voters available!")
            return
        print("\n===== Voter List =====")
        for voter in voters:
            print(voter.strip())


def search_voter():
    name = input("Enter voter Name or ID to Search: ").lower()
    found = False

    if not os.path.exists("data/voters.txt"):
        print("No data found!")
        return

    with open("data/voters.txt", "r") as file:
        for line in file:
            # Check if the voter name (after the prefix) matches the search term.
            if name.lower() in line.lower():
                print(line.strip())
                found = True

    if not found:
        print("voter not found!")

def delete_voter():
    name = input("Enter voter Name or Id to Delete: ")

    if not os.path.exists("data/voters.txt"):
        print("No data found!")
        return

    with open("data/voters.txt", "r") as file:
        lines = file.readlines()

    with open("data/voters.txt", "w") as file:
        deleted = False
        for line in lines:
            # If the line (ignoring case) contains the voter name, remove it.
            if name.lower() in line.lower():
                deleted = True
                continue
            file.write(line)

    if deleted:
        print("voter deleted successfully!")
    else:
        print("voter not found!")