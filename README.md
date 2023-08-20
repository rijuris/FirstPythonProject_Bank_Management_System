# FirstPythonProject_Bank_Management_System

The program starts by initializing an empty dictionary to store account data. The class defines several methods to perform common banking operations:

open_account(): This method allows users to create a new bank account by entering their name, account number, phone number, and opening balance. Account information is stored in the dictionary as a data structure.

deposit(): Users can deposit money into their existing accounts by providing their account number and the deposit amount. The program checks if the account exists, updates the account balance, and confirms the deposit.

withdrawal(): For withdrawals, users enter their account number and the withdrawal amount. The system checks the account's existence and available balance, deducts the withdrawal amount, and provides feedback on the transaction's success.

check_balance(): This method enables users to check their account balance by providing their account number. It retrieves and displays the current balance.

close_account(): To close an account, users input their account number. If the account exists, it is removed from the dictionary, effectively closing it.

The program operates within a while loop that presents a menu of banking options (open account, deposit, withdrawal, check balance, close account, and exit) to the user. The user can select an option by entering a corresponding number. Invalid inputs prompt the system to display an error message.

When the program is executed (if "name" is "main"), it creates an instance of the Bank_Management_System class and initiates the main loop, allowing users to interact with the simulated bank management system. This code serves as a simplified, console-based banking application for educational purposes, with account data stored in memory rather than a database.

Acknowledgments:

I would like to express my sincere gratitude to my teacher, Siji Ma'am and ENTRI for their excellent guidance in teaching me Python. Their valuable support and expertise have been instrumental in developing this code.
