from config import current_date
from save_json import load_expenses, save_expense
from datetime import datetime

json_list = load_expenses()
def generate_id():
   if not json_list:
      return 1
   else:
      return json_list[-1]['id'] + 1
   

def add_expense(args):
    try:
        amount = float(args.amount)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
    except:
        print("Amount must be a positive number.")
        return
    
    expense = {
        'id' : generate_id(),
        'description' : args.description,
        'amount' : args.amount,
        'created_at' : current_date,
        'updated_at' : None
    }

    json_list.append(expense)
    save_expense(json_list)

    print(f"Expense added successfully! ID: {expense['id']}")

def update_expense(args):
    if not json_list:
        print("No expense to update.")
        return

    expense_id = int(args.id)

    for item in json_list:
        if item['id'] == expense_id:
            updated = False

            if args.description is not None:
                item['description'] = args.description
                updated = True

            if args.amount is not None:
                item['amount'] = args.amount
                updated = True

            if updated:
                item['updated_at'] = current_date
                save_expense(json_list)
                print(f"Expense {expense_id} updated successfully.")
            else:
                print("Nothing to update.")

            return

    print(f"Expense {expense_id} not found.")

def delete_expense(args):
    if not json_list:
        print("No expense to delete.")
        return

    expense_id = int(args.id)

    for item in json_list:
        if item['id'] == expense_id:
            json_list.remove(item)
            save_expense(json_list)
            print(f"Expense {expense_id} deleted successfully.")
            return

    print(f"Expense with ID {expense_id} not found.")

def list_expense(args):
    if not json_list:
        print("No expense found.")
        return

    for item in json_list:
        print(
            f'[ID {item["id"]}] {item["description"]}\n'
            f'{"Amount":12}: {item["amount"]}\n'
            f'{"Created at":12}: {item["created_at"]}\n'
            f'{"Updated at":12}: {item["updated_at"]}\n'
            f'{"-" * 40}'
        )

def sum_expense(args):
    month = args.month
    total = 0

    if not json_list:
        print("No expense found.")
        return

    if month is None:
        for item in json_list:
            total += int(item['amount'])

        print(f"Total expenses: {total}")
        return

    month = int(month)

    for item in json_list:
        created_month = datetime.strptime(
            item['created_at'], '%Y-%m-%d %H:%M:%S'
        ).month

        if created_month == month:
            total += int(item['amount'])

    print(f"Total expenses for month {month}: {total}")


