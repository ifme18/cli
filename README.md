

Bank CLI Application

Overview

The Bank CLI application is a command-line tool for managing bank branches and accounts. It provides functionality to create branches, add accounts, update account balances, delete accounts, transfer funds, and view account or branch details.

This application is built using Python with SQLAlchemy for database operations and uses an SQLite database named bank.db.

Features

Create a new branch: Add a new bank branch with a name and location.

Add a new account: Add a new account to an existing branch with a holder's name and starting balance.

Update account balance: Modify the balance of an existing account.

Delete an account: Remove an account from the database.

View all members in a branch: List all accounts in a specific branch.

Transfer funds between accounts: Transfer money between two accounts.

View account details: Display details of a specific account.

View branch details: Display details of a specific branch, including its accounts.

View total branch balance: Calculate and display the total balance of all accounts in a branch.

Exit: Close the application.

Prerequisites

Python 3.7 or higher

SQLAlchemy library

Setup

Clone or download this repository.

Install the required dependencies by running:

pip install sqlalchemy

Ensure the models.py file defines the following:

A Branch class representing a bank branch.

A BankAccount class representing bank accounts.

A relationship between Branch and BankAccount (e.g., Branch.accounts to list all accounts in a branch).

Create the SQLite database by running the SQLAlchemy models.

Run the application using:

python main.py

Usage

Follow the menu options displayed in the CLI to interact with the application.

Enter the corresponding number for the desired operation.

Provide the required details when prompted.

Example Workflow

Creating a Branch:

Select option 1 from the menu.

Enter the branch name and location.

Adding an Account:

Select option 2 from the menu.

Provide the branch ID, holder's name, and starting balance.

Transferring Funds:

Select option 6 from the menu.

Enter the sender account ID, receiver account ID, and transfer amount.

Database Schema

Branch

id: Primary Key

name: Branch name

location: Branch location

accounts: Relationship to BankAccount

BankAccount

id: Primary Key

holdersname: Name of the account holder

balance: Account balance

branch_id: Foreign Key to Branch
