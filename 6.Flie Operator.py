# PR. 6 File Operator 

import os
import datetime

class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        text = input("\nEnter your journal entry: ")

        if text.strip() == "":
            print("Entry cannot be empty.")
            return

        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            
            if os.path.exists(self.filename) == False:
                f = open(self.filename, "x")
                f.close()

            
            f = open(self.filename, "a")
            f.write("[" + date + "]\n")
            f.write(text + "\n\n")
            f.close()

            print("\nEntry added successfully!")

        except FileExistsError:
            print("File already exists.")

        except PermissionError:
            print("No permission to write in the file.")

    def view_entries(self):
        try:
            
            f = open(self.filename, "r")
            data = f.read()
            f.close()

            if data.strip() == "":
                print("\nNo journal entries found.")
                return

            entries = data.strip().split("\n\n")

            print("\nYour Journal Entries:")
            print("-" * 35)

            for entry in reversed(entries):
                print(entry)
                print()

        except FileNotFoundError:
            print("\nNo journal entries found.")

        except PermissionError:
            print("No permission to read the file.")

    def search_entry(self):
        keyword = input("\nEnter keyword or date: ").strip()

        if keyword == "":
            print("Please enter something to search.")
            return

        try:
            
            f = open(self.filename, "r")
            data = f.read()
            f.close()

            entries = data.strip().split("\n\n")
            found = False

            print("\nMatching Entries:")
            print("-" * 35)

            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry)
                    print()
                    found = True

            if found == False:
                print("No entry found.")

        except FileNotFoundError:
            print("\nNo journal entries found.")

        except PermissionError:
            print("No permission to read the file.")

    def delete_entries(self):
        if os.path.exists(self.filename) == False:
            print("\nNo journal entries to delete.")
            return

        confirm = input(
            "\nAre you sure you want to delete all entries? (yes/no): "
        ).lower()

        if confirm == "yes":
            try:
                
                f = open(self.filename, "w")
                f.close()

                os.remove(self.filename)

                print("\nAll journal entries deleted.")

            except PermissionError:
                print("No permission to delete the file.")

        else:
            print("\nDeletion cancelled.")

    def run(self):
        print("Welcome to Personal Journal Manager!")

        while True:
            print("\n1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entries()

            elif choice == "5":
                print("\nThank you for using Personal Journal Manager.")
                break

            else:
                print("\nInvalid choice.")


journal = JournalManager()
journal.run()