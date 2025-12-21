# Expense Tracker CLI

A simple command-line expense tracker written in Python.  
This project allows you to manage personal expenses using a CLI application, with data persisted locally in a JSON file.

The project is based on the roadmap.sh Expense Tracker challenge: https://roadmap.sh/projects/expense-tracker

## Features

- Add a new expense with description and amount  
- Update an existing expense  
- Delete an expense by ID  
- List all expenses in a formatted output  
- Show total expenses  
- Show total expenses for a specific month  

## Commands

Examples of usage:

```bash
expense-tracker add --description "Lunch" --amount 20
expense-tracker list
expense-tracker summary
expense-tracker summary --month 8
expense-tracker update --id 2 --description "Dinner"
expense-tracker delete --id 2
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/expense-tracker.git
```

2. Enter the project directory:
```bash
cd expense-tracker
```

3. Run the application:
```bash
python main.py <command> [options]
```

## Data Storage

All expenses are stored locally in a JSON file.  
This ensures data persistence without the need for a database.

Each expense contains:
- id  
- description  
- amount  
- created_at  
- updated_at  

## Example Output

```text
[ID 1] Coffee
Description : Coffee
Amount      : 5
Created at  : 2025-12-05 14:23:11
Updated at  : N/A
----------------------------------------
```

## Monthly Summary

```bash
expense-tracker summary --month 12
```

Output:
```text
Total expenses for month 12: 45
```

## Project Purpose

This project was built for learning purposes, focusing on:
- Python CLI development
- Argument parsing with argparse
- File handling with JSON
- Basic CRUD operations

## License

MIT License
