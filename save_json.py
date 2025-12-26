import json
import os
import sys
from config import DATA_FILE


def create_json_file():
    """Create a blank JSON file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'w', encoding='utf-8') as file:
                json.dump([], file)
        except OSError as e:
            print(f'Error: Unable to create data file: {e}')
            sys.exit(1)


def save_expense(expenses):
    """Save expenses to JSON file.
    
    Returns:
        bool: True if save was successful, False otherwise
    """
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(expenses, file, indent=4)
        return True
    except OSError as e:
        print(f'Error: Unable to save expenses to disk: {e}')
        return False


def load_expenses():
    """Load expenses from JSON file.
    
    Returns:
        list: List of expenses, or empty list if file doesn't exist or is invalid
    """
    create_json_file()
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f'Warning: Expense data could not be loaded (invalid JSON): {e}')
        print('Starting with an empty list.')
        return []
    except OSError as e:
        print(f'Error: Unable to read data file: {e}')
        return []
