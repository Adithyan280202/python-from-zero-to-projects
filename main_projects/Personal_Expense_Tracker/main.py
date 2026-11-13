
# Personal Expense Tracker - Version 1.0

print("================================")
print("     PERSONAL EXPENSE TRACKER")
print("================================")

expenses = []

choice = 0

while choice != 4:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        name = input("Enter expense name: ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("\nExpense added successfully!")

    elif choice == 2:

        print("\n--------- EXPENSE LIST ---------")

        if len(expenses) == 0:
            print("No expenses recorded.")

        else:
            for expense in expenses:
                print("Name:", expense["name"])
                print("Category:", expense["category"])
                print("Amount:", expense["amount"])
                print("--------------------------")

    elif choice == 3:

        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("\nTotal Expenses: ₹", total)

    elif choice == 4:
        print("\nThank you for using Expense Tracker!")

    else:
        print("\nInvalid choice. Try again.")
