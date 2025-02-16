import os

def get_candidates():
    """Reads the candidate list and extracts serial numbers, names, and marks."""
    candidates = []
    if not os.path.exists("data/candidates.txt"):
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
                candidates.append((serial_no, candidate_name, mark))
            except IndexError:
                continue  # Skip malformed lines

    return candidates

def has_voted(voter_id):
    """Check if the voter has already voted."""
    if not os.path.exists("data/votes.txt"):
        return False  # No votes recorded yet

    with open("data/votes.txt", "r") as file:
        for line in file:
            recorded_id = line.strip().split(" ")[0]  # First field is voter ID
            if recorded_id == voter_id:
                return True
    return False

def is_registered_voter(voter_id, voter_name):
    """Check if the voter is registered."""
    if not os.path.exists("data/voters.txt"):
        return False  # No registered voters

    with open("data/voters.txt", "r") as file:
        for line in file:
            parts = line.strip().split("   ")  # Split by triple spaces
            if len(parts) < 2:
                continue
            existing_id = parts[0].split(":")[1].strip()  # Extract voter ID
            existing_name = parts[1].split(":")[1].strip()  # Extract voter Name
            if existing_id == voter_id and existing_name.lower() == voter_name.lower():
                return True
    return False

def cast_vote():
    """Allow only registered voters to vote once for a valid candidate."""
    candidates = get_candidates()

    if not candidates:
        print("No candidates available! Please add candidates first.")
        return

    voter_name = input("Enter your Name: ").strip()
    voter_id = input("Enter your Voter ID: ").strip()

    if not is_registered_voter(voter_id, voter_name):
        print("You are not a registered voter! Vote denied.")
        return

    if has_voted(voter_id):
        print("You have already voted! Multiple votes are not allowed.")
        return

    print("\n===== Cast Your Vote =====")
    for candidate in candidates:
        print(f"{candidate[0]}. {candidate[1]} - Mark: {candidate[2]}")  # Show serial number, candidate name, and mark

    choice = input("Enter the candidate's serial number to vote: ").strip()

    if not any(candidate[0] == choice for candidate in candidates):
        print("Invalid input! Vote not recorded.")
        return

    with open("data/votes.txt", "a") as file:
        file.write(f"{voter_id} {choice}\n")  # Record: voter_id candidate_serial

    print("Your vote has been successfully recorded!")

# Run the voting function
if __name__ == "__main__":
    cast_vote()
