import json
import os

class BankSystem:
    def __init__(self):
        self.data_file = "bank_data.json"
        self.accounts = self.load_data()

    def load_data(self):
        
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    content = f.read().strip()
                    return json.loads(content) if content else {}
            except (json.JSONDecodeError, ValueError):
                return {}
        return {}

    def save_data(self):
        """Saves current accounts to the JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.accounts, f, indent=4)

    def create_account(self):
        print("---  Open New Account ---")
        name = input("Enter your full name: ").strip().title()
        if name in self.accounts:
            print(" Error: An account with this name already exists.")
            return
        
        try:
            initial_deposit = float(input("Enter initial deposit amount: ₹"))
            if initial_deposit < 0:
                print(" Error: Initial deposit cannot be negative.")
                return
            self.accounts[name] = initial_deposit
            self.save_data()
            print(f" Success! Account created for {name} with ₹{initial_deposit}")
        except ValueError:
            print(" Error: Invalid amount entered.")

    def check_balance(self):
        name = input("\nEnter your account name: ").strip().title()
        if name in self.accounts:
            print(f"  Current Balance for {name}: ₹{self.accounts[name]}")
        else:
            print("  Error: Account not found.")

    def deposit(self):
        name = input("Enter account name for deposit: ").strip().title()
        if name in self.accounts:
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount > 0:
                    self.accounts[name] += amount
                    self.save_data()
                    print(f"Deposited ₹{amount}. New Balance: ₹{self.accounts[name]}")
                else:
                    print(" Error: Amount must be positive.")
            except ValueError:
                print("Error: Invalid amount entered.")
        else:
            print(" Error: Account not found.")

    def withdraw(self):
        name = input("\nEnter account name for withdrawal: ").strip().title()
        if name in self.accounts:
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if 0 < amount <= self.accounts[name]:
                    self.accounts[name] -= amount
                    self.save_data()
                    print(f"  Withdrew ₹{amount}. Remaining Balance: ₹{self.accounts[name]}")
                elif amount > self.accounts[name]:
                    print(" Error: Insufficient funds!")
                else:
                    print("  Error: Amount must be positive.")
            except ValueError:
                print(" Error: Invalid amount entered.")
        else:
            print(" Error: Account not found.")

def main_menu():
    bank = BankSystem()
    while True:
        print("\n" + "="*35)
        print("   VIT COMMUNITY BANK")
        print("="*35)
        print(" 1. Create New Account")
        print(" 2. Check Balance")
        print(" 3. Deposit Money")
        print(" 4. Withdraw Money")
        print(" 5. Exit")
        
        choice = input(" Select an option (1-5): ")

        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.check_balance()
        elif choice == '3':
            bank.deposit()
        elif choice == '4':
            bank.withdraw()
        elif choice == '5':
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
