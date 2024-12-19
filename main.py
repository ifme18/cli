from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Branch, BankAccount

DATABASE_URL = "sqlite:///bank.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_branch():
    name = input("Enter the branch name: ")
    location = input("Enter the branch location: ")
    new_branch = Branch(name=name, location=location)
    session.add(new_branch)
    session.commit()
    print(f"Branch '{name}' created successfully.")

def add_member():
    branch_id = int(input("Enter the bank branch ID: "))
    holdersname = input("Enter the account holder's name: ")
    balance = float(input("Enter the starting balance: "))
    new_account = BankAccount(holdersname=holdersname, balance=balance, branch_id=branch_id)
    session.add(new_account)
    session.commit()
    print(f"Account created for {holdersname} with balance {balance}.")

def update_balance():
    account_id = int(input("Enter the account ID: "))
    new_balance = float(input("Enter the new balance: "))
    account = session.query(BankAccount).filter_by(id=account_id).first()
    if account:
        account.balance = new_balance
        session.commit()
        print(f"Account {account_id} balance updated to {new_balance}.")
    else:
        print("Account not found.")

def delete_account():
    account_id = int(input("Enter the account ID to delete: "))
    account = session.query(BankAccount).filter_by(id=account_id).first()
    if account:
        session.delete(account)
        session.commit()
        print(f"Account {account_id} deleted successfully.")
    else:
        print("Account not found.")

def view_members():
    branch_id = int(input("Enter the bank branch ID: "))
    branch = session.query(Branch).filter_by(id=branch_id).first()
    if branch:
        print(f"Accounts in branch '{branch.name}':")
        for account in branch.accounts:
            print(f"- ID: {account.id}, Holder: {account.holdersname}, Balance: {account.balance}")
    else:
        print("Branch not found.")

def transfer_funds():
    from_account_id = int(input("Enter the sender account ID: "))
    to_account_id = int(input("Enter the receiver account ID: "))
    amount = float(input("Enter the transfer amount: "))

    from_account = session.query(BankAccount).filter_by(id=from_account_id).first()
    to_account = session.query(BankAccount).filter_by(id=to_account_id).first()

    if from_account and to_account and from_account.balance >= amount:
        from_account.balance -= amount
        to_account.balance += amount
        session.commit()
        print(f"Transferred {amount} from account {from_account_id} to {to_account_id}.")
    else:
        print("Transfer failed. Ensure accounts exist and sufficient balance.")

def view_account_details():
    account_id = int(input("Enter the account ID: "))
    account = session.query(BankAccount).filter_by(id=account_id).first()
    if account:
        print(f"Account ID: {account.id}, Holder: {account.holdersname}, Balance: {account.balance}")
    else:
        print("Account not found.")

def view_branch_details():
    branch_id = int(input("Enter the bank branch ID: "))
    branch = session.query(Branch).filter_by(id=branch_id).first()
    if branch:
        print(f"Branch ID: {branch.id}, Name: {branch.name}, Location: {branch.location}")
        print("Accounts in this branch:")
        for account in branch.accounts:
            print(f"- ID: {account.id}, Holder: {account.holdersname}, Balance: {account.balance}")
    else:
        print("Branch not found.")

def view_total_branch_balance():
    branch_id = int(input("Enter the bank branch ID: "))
    branch = session.query(Branch).filter_by(id=branch_id).first()
    if branch:
        total_balance = sum(account.balance for account in branch.accounts)
        print(f"Total balance in branch '{branch.name}': {total_balance}")
    else:
        print("Branch not found.")

# List of menu options
menu_options = [
    "Create a new branch",
    "Add a new account",
    "Update account balance",
    "Delete an account",
    "View all members in a branch",
    "Transfer funds between accounts",
    "View account details",
    "View branch details",
    "View total branch balance",
    "Exit"
]


actions = {
    "1": create_branch,
    "2": add_member,
    "3": update_balance,
    "4": delete_account,
    "5": view_members,
    "6": transfer_funds,
    "7": view_account_details,
    "8": view_branch_details,
    "9": view_total_branch_balance
}

def main():
    while True:
        print("\nBank CLI Menu:")
        for i, option in enumerate(menu_options, 1):
            print(f"{i}. {option}")

        choice = input("Enter your choice (1-10): ")

        if choice in actions:
            actions[choice]() 
        elif choice == "10":
            print("Exiting Bank CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
