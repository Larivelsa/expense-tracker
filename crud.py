from config import get_current_date
from save_json import load_expenses, save_expense
from datetime import datetime


def generate_id(expenses):
    """Generate a new unique ID for an expense.
    
    Args:
        expenses: List of existing expenses
        
    Returns:
        int: Next available ID (1 if list is empty)
    """
    if not expenses:
        return 1
    return max(expense['id'] for expense in expenses) + 1


def validate_amount(amount_str):
    """Validate and convert amount string to float.
    
    Args:
        amount_str: String representation of amount
        
    Returns:
        float: Validated amount, or None if invalid
    """
    try:
        amount = float(amount_str)
        if amount <= 0:
            print("Error: Amount must be a positive number.")
            return None
        return amount
    except (ValueError, TypeError):
        print("Error: Amount must be a valid positive number.")
        return None


def validate_expense_id(id_str):
    """Validate and convert expense ID string to integer.
    
    Args:
        id_str: String representation of expense ID
        
    Returns:
        int: Validated ID, or None if invalid
    """
    try:
        expense_id = int(id_str)
        if expense_id <= 0:
            print("Error: Expense ID must be a positive integer.")
            return None
        return expense_id
    except (ValueError, TypeError):
        print("Error: Expense ID must be a valid positive integer.")
        return None


def validate_month(month_str):
    """Validate month parameter.
    
    Args:
        month_str: String representation of month (1-12)
        
    Returns:
        int: Validated month, or None if invalid
    """
    try:
        month = int(month_str)
        if month < 1 or month > 12:
            print("Error: Month must be between 1 and 12.")
            return None
        return month
    except (ValueError, TypeError):
        print("Error: Month must be a valid integer between 1 and 12.")
        return None


def add_expense(args):
    """Add a new expense to the tracker."""
    expenses = load_expenses()
    
    # Validate amount
    amount = validate_amount(args.amount)
    if amount is None:
        return
    
    # Validate description
    description = args.description.strip()
    if not description:
        print("Error: Description cannot be empty.")
        return
    
    expense = {
        'id': generate_id(expenses),
        'description': description,
        'amount': amount,  # Store as number, not string
        'created_at': get_current_date(),
        'updated_at': None
    }
    
    expenses.append(expense)
    
    if save_expense(expenses):
        print(f"Expense added successfully! ID: {expense['id']}")


def update_expense(args):
    """Update an existing expense."""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found to update.")
        return
    
    # Validate expense ID
    expense_id = validate_expense_id(args.id)
    if expense_id is None:
        return
    
    # Find and update expense
    for item in expenses:
        if item['id'] == expense_id:
            updated = False
            
            if args.description is not None:
                description = args.description.strip()
                if not description:
                    print("Error: Description cannot be empty.")
                    return
                item['description'] = description
                updated = True
            
            if args.amount is not None:
                amount = validate_amount(args.amount)
                if amount is None:
                    return
                item['amount'] = amount  # Store as number
                updated = True
            
            if updated:
                item['updated_at'] = get_current_date()
                if save_expense(expenses):
                    print(f"Expense with ID {expense_id} updated successfully.")
            else:
                print("No changes specified. Nothing to update.")
            return
    
    print(f"Error: Expense with ID {expense_id} not found.")


def delete_expense(args):
    """Delete an expense by ID."""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found to delete.")
        return
    
    # Validate expense ID
    expense_id = validate_expense_id(args.id)
    if expense_id is None:
        return
    
    # Find and remove expense
    for i, item in enumerate(expenses):
        if item['id'] == expense_id:
            expenses.pop(i)
            if save_expense(expenses):
                print(f"Expense with ID {expense_id} deleted successfully.")
            return
    
    print(f"Error: Expense with ID {expense_id} not found.")


def list_expense(args):
    """List all expenses."""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    for item in expenses:
        updated_at = item.get('updated_at') or 'N/A'
        print(
            f'[ID {item["id"]}] {item["description"]}\n'
            f'{"Amount":12}: {item["amount"]}\n'
            f'{"Created at":12}: {item["created_at"]}\n'
            f'{"Updated at":12}: {updated_at}\n'
            f'{"-" * 40}'
        )


def sum_expense(args):
    """Calculate total expenses, optionally filtered by month."""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    total = 0.0
    
    if args.month is None:
        # Sum all expenses
        for item in expenses:
            total += float(item['amount'])
        print(f"Total expenses: {total:.2f}")
        return
    
    # Validate and filter by month
    month = validate_month(args.month)
    if month is None:
        return
    
    for item in expenses:
        try:
            created_month = datetime.strptime(
                item['created_at'], '%Y-%m-%d %H:%M:%S'
            ).month
            if created_month == month:
                total += float(item['amount'])
        except (ValueError, KeyError) as e:
            # Skip expenses with invalid date format
            continue
    
    print(f"Total expenses for month {month}: {total:.2f}")


