Bank CLI Application

Overview

The Bank CLI Application is a command-line tool for managing bank branches and accounts. It provides functionalities for creating branches, adding accounts, updating account balances, deleting accounts, and viewing account details within a branch. The application uses SQLite as the database and SQLAlchemy for ORM.

Prerequisites

Python 3.7+

SQLite database

SQLAlchemy library

models.py file defining the Branch and BankAccount models

Installation

Clone or download the repository.

Install the required dependencies:

pip install sqlalchemy

Ensure that the models.py file contains the following models:

Branch: Represents a bank branch with attributes id, name, and location.

BankAccount: Represents a bank account with attributes id, holdersname, balance, and branch_id (foreign key referencing Branch).

Usage

Run the application using the following command:

python main.py

Features

1. Create a New Branch

Allows the user to add a new bank branch by specifying its name and location.

Data is saved in the Branch table of the database.

2. Add a New Account

Allows the user to create a new account by specifying the branch ID, account holder's name, and initial balance.

Data is saved in the BankAccount table with a foreign key linking it to the branch.

3. Update Account Balance

Updates the balance of an existing account by specifying the account ID and the new balance.

4. Delete an Account

Deletes an existing account by specifying the account ID.

5. View All Members in a Branch

Lists all accounts within a specified branch by providing the branch ID.

6. Exit

Exits the application.
