# py_project.6--Flie-Operator


Personal Journal Manager

Creat By : Ayush Jivani

Language : Python


explin video link :https://drive.google.com/file/d/142FHiyVC5kMPQNeb3Br3n1WKGMeMrB2s/view?usp=drive_link


repositories link :https://github.com/ayushjivani082/py_project.6--Flie-Operator/blob/896632d8cabc560a257507394abaededbf652232/6.Flie%20Operator.py

A simple Python project for creating and managing a personal journal using text file handling.
About The Project


This project allows the user to:
Add a new journal entry
View all journal entries
Search an entry using a keyword or date
Delete all journal entries
Exit from the program
All journal entries are stored in journal.txt.



Features
1. Add New Entry
The user can enter a journal entry. A date and time are automatically added to the entry.
2. View All Entries
The program reads the journal.txt file and displays all saved entries.
3. Search Entry
The user can search for an entry by entering a keyword or date.
4. Delete All Entries
The user can delete all journal entries after confirmation.
5. Exit
The user can safely exit the program from the main menu.
File Handling



This project demonstrates four file opening modes:
r  -> Read the file
w  -> Clear/write the file
a  -> Add new data at the end
x  -> Create a new file



OOP Used
The project uses a class named:
JournalManager
The class contains methods for:
add_entry()
view_entries()
search_entry()
delete_entries()
run()
An object is created to run the program:
journal = JournalManager()
journal.run()
Exception Handling
The program handles common file errors:
FileNotFoundError
PermissionError
FileExistsError
This helps prevent the program from crashing during common file operations.
Modules Used
import os
import datetime
os
Used for checking and deleting the journal file.
datetime
Used for adding the current date and time to journal entries.
Project Menu
Welcome to Personal Journal Manager!

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
Requirements
Python 3.x
Any Python IDE or code editor
How To Run
Download the project.
Open the Python file.
Run the program.
Select an option from the menu.
Add and manage your journal entries.



Author
Ayush Jivani


Project Name
PR. 6 File Operator - Personal Journal Manager


Learning Outcome
Through this project, I learned:
Python file handling

r, w, a, and x file modes

Reading and writing text files

Exception handling

Classes and objects

Menu-driven programs

Using os and datetime modules
