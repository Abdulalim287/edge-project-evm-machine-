Electronic Voting Machine (EVM) Project Report

1. Introduction: The Electronic Voting Machine (EVM) project is a Python-based system designed to facilitate secure and efficient electronic voting. This system enables voters to cast their votes electronically, ensuring accuracy, transparency, and integrity in the electoral process. The project consists of multiple functionalities, including voter registration, candidate management, voting, and result calculation.
2. Objectives
•	To develop a user-friendly electronic voting system.
•	To ensure only registered voters can participate in elections.
•	To prevent duplicate voting.
•	To securely store votes and provide accurate results.
•	To allow administrators to manage candidates and voters efficiently.
3. System Features
 The system consists of two main modules:
 
i. Vote Casting Module
• Allows a voter to cast their vote.
ii. Admin Module
• The admin function is hidden.
• Type "admin" to enter the admin module.
• Then, enter the admin password.
• The default password is admin123.

A.	Vote casting Module:
 
a. To vote, you must enter your name and ID.
b. If the name and ID don’t match, you cannot cast a vote.
c. Each voter can cast only one vote.
d. Then, you will see the list of candidates.
e. To cast your vote, enter the candidate's number.
B.	Admin Module
 
This panel allows you to perform the following actions:
a. Manage candidates.
b. Manage voters.
c. View election results.
d. Add, view, search, and delete candidates.
e. Add, view, search, and delete voter records.
f. Display election results, including vote counts and the winner.
(1) Manage candidates:
 
Allowing to do:
1. Add Candidate:
To add a candidate, provide the following details:
I.	Enter Candidate Name
II.	Enter Symbol/Mark
III.	Enter Party Name
2. View All Candidates
3. Search Candidates by Name
4. Delete Candidate
5. Return to Main Menu

(2) Manage Voters:
 
	Allowing to do:
		1.  Add voter
			To add voter provide:
			a. Enter Voter Name:
			b.  Enter Voter ID:
c.  Enter Birth Day (DD MM YYYY):
		2.  View all voter
		3.  Search voter by name
		4.  Delete voter 
		5. Return to admin menu
(3)  View Election Results:
 
Providing two options:
 1. Viewing result.
 
It show the number and percentage of vote  for each candidate, show winner candidate with vote.
2.  Erasing all result.
This section providing to delete all vote to admin . But must enter admin password.
Data Storage
	All data stored in a folder named data with three files.
•	Candidate data is stored in candidates.txt with the format:
SI_NO:1  Candidate Name:ABDUL HAKIM  Mark:DARIPALLAH  Party:JAMAYAT
•	Voter data is stored in voters.txt with the format:
ID:0001   Name:alim   Birth-date:15 11 2000
•	Votes are stored in votes.txt in the format:
Voter_ID Candidate_Serial
•	
4. Implementation The project is implemented using Python with file handling for data storage. The core functions include:
•	is_registered_voter(voter_id, name): Ensures only valid voters can vote.
•	has_voted(voter_id): Checks if a voter has already cast a vote.
•	cast_vote(): Handles the voting process securely.
•	add_candidate(), view_candidates(), search_candidate(), delete_candidate(): Manage candidates.
•	add_voter(), view_voters(), search_voter(), delete_voter(): Manage voter records.
•	calculate_results(): Computes and displays election results.
5. Security Measures
•	Prevents duplicate voter registration.
•	Ensures a voter can vote only once.
•	Validates correct input formats.
•	Secures stored data from unauthorized modifications.
6. Results and Analysis The system provides a fair and reliable voting platform. Test cases have been conducted to verify:
•	Only registered voters can vote.
•	Voters cannot vote more than once.
•	Admins can manage voter and candidate data effectively.
•	Results are calculated correctly based on stored votes.
7. Conclusion The EVM project successfully provides an efficient, secure, and transparent electronic voting solution. It eliminates common voting irregularities such as multiple voting and manual counting errors. Future enhancements could include a graphical user interface (GUI) and database integration for better performance and security.
8. Future Improvements
•	Implementing a database system for better data management.
•	Adding a graphical user interface (GUI) for enhanced usability.
•	Introducing encryption fingerprint biometric techniques for securing vote data.
•	Enhancing authentication with biometric or OTP verification.
This project serves as a foundation for developing more advanced electronic voting systems suitable for larger-scale elections.


