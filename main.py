class Bank_Management_System:
    def __init__(self):
        # Initialize an empty dictionary to store account data
        self.accounts = {}

    def open_account(self):
        # Prompt the user for account information
        name = input("Enter the name: ")
        account_no = input("Enter your account number: ")
        phone_no = input("Enter your phone number: ")
        opening_balance = float(input("Enter the opening balance: "))

        # Store the account data in the dictionary
        self.accounts[account_no] = {
            'name': name,
            'phone_no': phone_no,
            'balance': opening_balance
        }

        print("Account opened successfully.")

    def deposit(self):
        # Prompt the user for account number and deposit amount
        account_no = input("Enter your account number: ")
        amount = float(input("Enter the deposit amount: "))

        # Check if the account exists in the dictionary
        if account_no in self.accounts:
            # Update the account balance with the deposited amount
            self.accounts[account_no]['balance'] += amount
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdrawal(self):
        # Prompt the user for account number and withdrawal amount
        account_no = input("Enter your account number: ")
        amount = float(input("Enter the withdrawal amount: "))

        # Check if the account exists in the dictionary
        if account_no in self.accounts:
            # Check if there is enough balance for the withdrawal
            if self.accounts[account_no]['balance'] >= amount:
                # Update the account balance after withdrawal
                self.accounts[account_no]['balance'] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def check_balance(self):
        # Prompt the user for account number
        account_no = input("Enter your account number: ")

        # Check if the account exists in the dictionary
        if account_no in self.accounts:
            # Retrieve and display the current account balance
            balance = self.accounts[account_no]['balance']
            print(f"Your current balance on account {account_no} is {balance}")
        else:
            print("Account not found.")

    def close_account(self):
        # Prompt the user for account number
        account_no = input("Enter your account number: ")

        # Check if the account exists in the dictionary
        if account_no in self.accounts:
            # Remove the account from the dictionary to close it
            del self.accounts[account_no]
            print("Account closed successfully.")
        else:
            print("Account not found.")

    def main(self):
        while True:
            print('''
                1. OPEN AN ACCOUNT
                2. DEPOSIT
                3. WITHDRAWAL
                4. CHECK YOUR BALANCE
                5. CLOSE AN ACCOUNT
                6. EXIT
            ''')
            choice = input("Enter your option from 1 to 6: ")
            if choice == '1':
                self.open_account()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdrawal()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                self.close_account()
            elif choice == '6':
                print("Exiting the Bank Management System. Goodbye!")
                break
            else:
                print("Oops! Invalid Input, please choose between 1 to 6")

if __name__ == "__main__":
    # Create an instance of the Bank_Management_System class and run the main loop
    bank_system = Bank_Management_System()
    bank_system.main()
