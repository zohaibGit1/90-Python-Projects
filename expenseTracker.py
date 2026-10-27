import os
import json

FILENAME = "expenses.json"

class ExpenseTracker:
    def addExpense(self, ID, Description, Amount, Cateegory) -> dict:
        expense = {}
        # 1. Load existing data if file exists and has content
        if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
            try:
                with open(FILENAME, "r") as f:
                    expense = json.load(f)
            except json.JSONDecodeError:
                expense = {}
        # 2. Add the new expense record under the given ID
        if str(ID) in expense:
            expectation = input(f"Expense with ID {ID} already exists. Do you want to overwrite it? (yes/no): ").strip().lower()
            if expectation != "yes":
                print("Expense not added.")
                return expense

        expense[str(ID)] = {
            "description": Description,
            "amount": Amount,
            "category": Cateegory
        }
        # 3. Save the updated dictionary back to the JSON file
        with open(FILENAME, "w") as f:
            json.dump(expense, f, indent=4)
        return expense 


    def viewAllExpense(self) -> None:

        if os.path.exists(FILENAME) and os.path.getsize(FILENAME) == 0:
            print("No expense found")

        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Error: expenses.json file is corrupted or empty.")
            return

        if not data:
            print("No Expense Found")
            return

        for exp_id, details in data.items():
            desc = details.get("description", "")
            amount = details.get("amount", 0)
            category = details.get("category", "")

            # Formatting with spacing for clean alignment
            print(
                f"ID: {exp_id:<2} | Description: {desc:<10} | Amount: ₹{amount:<2} | Category: {category}"
            )

    def totalExpense(self) -> list:

        if os.path.exists(FILENAME) and os.path.getsize(FILENAME) == 0:
            print("No expense found")
        
        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Error: expenses.json file is corrupted or empty.")
            return

        if not data:
            print("No Expense Found")
            return

        total_spending = sum(float(details.get("amount", 0)) for details in data.values())
        total_expense = len(data)

        print(f"Total Expense: {total_expense}")
        print(f"Total Spending: ₹{total_spending:2f}") 

        return total_expense, total_spending

    def CategoryWiseSpending(self) -> None:
        # Load existing expenses
        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No expense found.")
            return

        if not data:
            print("No expense found.")
            return

        category_total = {}

        for details in data.items():
            category = details.get("category", "")
            amount = float(details.get("amount", 0))z

            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount

        for category, amount in category_total.items():
            print(f"{category}: ₹{amount:.2f}")

    def deleteExpense(self, ID) -> None:
        if os.path.exists(FILENAME) and os.path.getsize(FILENAME) == 0:
            print("No expense found")
            return

        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Error: expenses.json file is corrupted or empty.")
            return
        except FileNotFoundError:
            print("Error: expenses.json file not found.")
            return

        if str(ID) in data:
            del data[str(ID)]
            with open(FILENAME, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Expense with ID {ID} has been deleted.")
        else:
            print(f"No expense found with ID {ID}.")


    def highestExpense(self) -> None:
        if os.path.exists(FILENAME) and os.path.getsize(FILENAME) == 0:
            print("No expense found")
            return

        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Error: expenses.json file is corrupted or empty.")
            return

        if not data:
            print("No Expense Found")
            return

        highest_expense = max(data.items(), key=lambda x: float(x[1].get("amount", 0)))
        print(f"Highest Expense: {highest_expense[0]} - ₹{highest_expense[1].get('amount', 0)}")

    def LowestExpense(self) -> None:
            if os.path.exists(FILENAME) and os.path.getsize(FILENAME) == 0:
                print("No expense found")
                return
    
            try:
                with open(FILENAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print("Error: expenses.json file is corrupted or empty.")
                return
    
            if not data:
                print("No Expense Found")
                return
    
            lowest_expense = min(data.items(), key=lambda x: float(x[1].get("amount", 0)))
            print(f"Lowest Expense: {lowest_expense[0]} - ₹{lowest_expense[1].get('amount', 0)}")
        

def menu():
    while True:
        print("\n ========== SMART EXPENSE TRACKER ========== ")
        print("1. Add Expenses ")
        print("2. View All Expenses ")
        print("3. Total Expenses ")
        print("4. Category Wise Spending ")
        print("5. Delete Expense ")
        print("6. Highest Expense ")
        print("7. Lowest Expense ")
        print("8. Exit ")

        choice = input("Enter the user choice ").strip()
        obj1 = ExpenseTracker()
        if choice == "1":
            id = int(input("Enter the ID For the Expense "))
            desc = input("Enter the Description For the Expense")
            amt = float(input("Enter the Amount For the Expense "))
            cateegory = input("Enter the Category For the Expense ")        
            obj1.addExpense(id, desc, amt, cateegory)

        elif choice == "2":
            obj1.viewAllExpense()

        elif choice == "3":
            obj1.totalExpense()

        elif choice == "4":
            obj1.CategoryWiseSpending()

        elif choice == "5":
            obj1.deleteExpense(int(input("Enter the ID of the expense to delete: ")))

        elif choice == "6":
            obj1.highestExpense()       


        elif choice == "7":
            obj1.LowestExpense()    

        else:
            # Catches any text or number not specified above
                print("Invalid option! Please select a valid number from the menu.")
                break

if __name__ == "__main__":
    menu()

            




