# InternCircle Project 03: Personal Expense Tracker with CSV

A beginner-friendly Python command-line app for recording expenses, storing them persistently in a CSV file, filtering records, and viewing spending summaries.

## Features
- Add, view, and filter expenses.
- Save data in `expenses.csv` so records remain after restarting.
- Validate dates in `YYYY-MM-DD` format and reject negative or invalid amounts.
- Filter by category or month (`YYYY-MM`).
- Show totals for each category, the grand total, and the largest single expense.
- Create the CSV file with the required header automatically if it is missing.

## Requirements
- Python 3.10 or newer
- No external packages required; uses Python's built-in `csv`, `datetime`, and `pathlib` modules.

## Run
Open a terminal in this folder and run:

```bash
python expense_tracker.py
```

## Menu
1. Add expense
2. View all expenses
3. Filter expenses
4. Summary
5. Quit

When adding an expense, press Enter at the date prompt to use today's date. Amounts must be zero or greater.

## CSV format
The file uses these columns:

```csv
date,category,description,amount
2026-10-04,Food,Lunch,120.50
```

The included `expenses.csv` contains ten fictional sample entries across September and October 2026. These are made-up examples, not real personal or bank data. Replace or clear the sample rows if you want to start with a blank tracker.

## Example problem fixed
An invalid date such as `2026-13-45` could otherwise cause a failure or incorrect data entry. The program validates dates immediately with `datetime.strptime()` and asks again until the date is valid. It also rejects negative amounts.

## Project files
- `expense_tracker.py` — main application
- `expenses.csv` — sample data with ten fictional expense rows
- `test_expense_tracker.py` — automated tests
- `TESTING.md` — manual testing checklist
