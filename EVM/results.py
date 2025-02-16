import os

def get_candidates():
    """Reads the candidate list and extracts serial numbers, names, and marks."""
    candidates = {}
    if not os.path.exists("data/candidates.txt"):
        print("Candidates file not found!")
        return candidates

    with open("data/candidates.txt", "r") as file:
        for line in file:
            parts = line.strip().split("  ")  # Split by double spaces
            if len(parts) < 4:
                continue

            try:
                serial_no = parts[0].split(":")[1].strip(".")  # Extract SI_NO
                candidate_name = parts[1].split(":")[1].strip()  # Extract candidate name
                mark = parts[2].split(":")[1].strip()  # Extract mark
                candidates[serial_no] = {
                    "name": candidate_name,
                    "mark": mark,
                    "votes": 0  # Initialize vote count
                }
            except IndexError:
                continue  # Skip malformed lines

    return candidates

def count_votes():
    """Counts the votes for each candidate."""
    candidates = get_candidates()

    if not candidates:
        print("No candidates available!")
        return

    if not os.path.exists("data/votes.txt"):
        print("No votes have been cast yet!")
        return

    total_votes = 0
    with open("data/votes.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                voter_id, candidate_id = parts
                if candidate_id in candidates:
                    candidates[candidate_id]["votes"] += 1
                    total_votes += 1

    # Display results
    print("\n===== Election Results =====")
    for candidate_id, data in candidates.items():
        votes = data["votes"]
        percentage = (votes / total_votes * 100) if total_votes > 0 else 0
        print(f"{data['name']} (Mark: {data['mark']}, Candidate SI_NO: {candidate_id}) - Votes: {votes} ({percentage:.2f}%)")

    # Determine the winner
    winner = max(candidates, key=lambda x: candidates[x]["votes"], default=None)
    if winner and candidates[winner]["votes"] > 0:
        print(f"\n🏆 Winner: {candidates[winner]['name']} (Mark: {candidates[winner]['mark']}, Candidate SI_NO: {winner}) with {candidates[winner]['votes']} votes!")
    else:
        print("No winner. No votes cast.")

def delete_results():
    """Delete all election results with admin password verification."""
    password = input("Enter Admin Password to delete results: ")
    if password == "admin123":
        if os.path.exists("data/votes.txt"):
            confirm = input("Are you sure you want to delete all results? (yes/no): ").strip().lower()
            if confirm == "yes":
                os.remove("data/votes.txt")
                print("✅ All election results have been deleted successfully.")
            else:
                print("Deletion canceled.")
        else:
            print("No results to delete.")
    else:
        print("❌ Incorrect password! Access denied.")

def results_menu():
    """Manage election results menu."""
    while True:
        print("\n===== Results Menu =====")
        print("1. View Results")
        print("2. Delete All Results")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            count_votes()
        elif choice == "2":
            delete_results()
        elif choice == "3":
            print("Exiting results module...")
            break
        else:
            print("Invalid choice! Please try again.")

# Run results menu if executed as a script
if __name__ == "__main__":
    results_menu()
