import json
from datetime import date

with open("data.json", "r") as file:
    data = json.load(file)

income = data["income"]
expenses = data["expenses"]

print("===== EXPENSE TRACKER =====")

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Check Balance")
    print("4. View Expenses")
    print("5. Expense Summary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter income amount: "))

            if amount <= 0:
                print("Invalid amount!")
            else:
                income = amount
                data["income"] = income

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

                print("Income added:", income)

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "2":
        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Invalid amount!")
            else:
                category = input("Enter category: ").strip().title()

                if category == "":
                    print("Category cannot be empty!")
                else:
                    new_expense = {
                        "amount": amount,
                        "category": category,
                        "date": str(date.today())
                    }

                    expenses.append(new_expense)

                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)

                    print("Expense added:", amount)
                    print("Category:", category)
                    print("Date:", date.today())

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "3":
        total_expense = sum(item["amount"] for item in expenses)
        balance = income - total_expense

        print("\n===== BALANCE =====")
        print("Total Income:", income)
        print("Total Expense:", total_expense)
        print("Current Balance:", balance)

    elif choice == "4":
        print("\n===== ALL EXPENSES =====")

        if len(expenses) == 0:
            print("No expenses found!")
        else:
            for i, item in enumerate(expenses, start=1):
                print(
                    i,
                    ".",
                    item["category"],
                    "-",
                    item["amount"],
                    "-",
                    item.get("date", "No date")
                )

    elif choice == "5":
        print("\n===== EXPENSE SUMMARY =====")

        if len(expenses) == 0:
            print("No expenses found!")
        else:
            summary = {}

            for item in expenses:
                category = item["category"]
                amount = item["amount"]

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

            for category, amount in summary.items():
                print(category, ":", amount)

            total_expense = sum(item["amount"] for item in expenses)
            print("Total Expense:", total_expense)

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")
