# Welcome message
def welcome_message():
    print("Welcome to the Expense Tracker!")

# Function to log an expense
def log_expense(expenses):
    try:
        amount = float(input("Enter the expense amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    categories = ['Food', 'Transport', 'Entertainment']
    print(f"Select a category from the following: {', '.join(categories)}")
    category = input("Enter the expense category: ").capitalize()
    if category not in categories:
        print("Invalid category. Please try again.")
        return
    
    description = input("Enter a description of the expense: ")

    # Store the expense data
    expenses.append({'amount': amount, 'category': category, 'description': description})
    print("Expense logged successfully!\n")

# Function to display summary
def display_summary(expenses):
    total_amount = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal amount spent: ${total_amount:.2f}")

    category_totals = {}
    for expense in expenses:
        category = expense['category']
        category_totals[category] = category_totals.get(category, 0) + expense['amount']
    
    print("Amount spent in each category:")
    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")
    
    print("\nAll expenses:")
    for expense in expenses:
        print(f"Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}")

# Thank you message
def thank_you_message():
    print("\nThank you for using the Expense Tracker!")

def main():
    welcome_message()
    expenses = []

    while True:
        log_expense(expenses)
        more = input("Do you want to log another expense? (yes/no): ").strip().lower()
        if more != 'yes':
            break
    
    display_summary(expenses)
    thank_you_message()

if __name__ == "__main__":
    main()