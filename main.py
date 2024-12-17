# Expense Tracker 

def main():

    # Categories for expenses
    categories = {
        "food": 0.0,
        "transport": 0.0,
        "entertainment": 0.0,
        "others": 0.0
    }
    
    # Total daily expenses
    total_expenses = 0.0
    
    print("Daily Expense Tracker")
    print("----------------------")
    
    while True:
        print("\nCategories: " + ", ".join(categories.keys()))
        print("Type 'summary' to see the report or 'exit' to quit.")
        
        user_input = input("Enter category or command: ").lower()
        
        if user_input == "exit":
            break
        elif user_input == "summary":
            # Display summary
            print("\nExpense Summary:")
            print("----------------")
            if total_expenses == 0:
                print("No expenses added yet.")
            else:
                print(f"Total Expenses: ${total_expenses:.2f}")
                for category, amount in categories.items():
                    percentage = (amount / total_expenses) * 100 if total_expenses > 0 else 0
                    print(f"{category.capitalize()}: ${amount:.2f} ({percentage:.2f}%)")
            print("----------------")
        elif user_input in categories:
            try:
                amount = float(input(f"Enter amount for {user_input}: $"))
                if amount < 0:
                    print("Amount cannot be negative. Try again.")
                else:
                    categories[user_input] += amount
                    total_expenses += amount
                    print(f"Added ${amount:.2f} to {user_input}.")
            except ValueError:
                print("Invalid amount! Please enter a numeric value.")
        else:
            print("Invalid category or command. Please try again!")

    print("\nThank you for using the Daily Expense Tracker!")

# Run the program
main()
