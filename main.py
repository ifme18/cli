from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Branch, BankAccount

DATABASE_URL = "sqlite:///bank.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

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

def main():
    while True:
        print("\nBank CLI Menu:")
        print("1. Add a new account")
        print("2. Update account balance")
        print("3. Delete an account")
        print("4. View all members in a branch")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_member()
        elif choice == "2":
            update_balance()
        elif choice == "3":
            delete_account()
        elif choice == "4":
            view_members()
        elif choice == "5":
            print("Exiting Bank CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
