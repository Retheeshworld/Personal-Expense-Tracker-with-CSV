"""InternCircle Project 03: Personal Expense Tracker with CSV.

Python 3.10+
Run: python expense_tracker.py
"""

import csv
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.csv")
FIELDS = ["date", "category", "description", "amount"]
DEFAULT_CATEGORIES = ["Food", "Travel", "Study", "Bills", "Fun"]


def ensure_data_file() -> None:
    """Create the CSV file with a header if it does not exist."""
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def load_expenses() -> list[dict[str, str]]:
    """Load expenses from the CSV file, returning an empty list if missing."""
    ensure_data_file()
    try:
        with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except OSError as error:
        print(f"Could not read expenses: {error}")
        return []


def save_expense(expense: dict[str, str]) -> None:
    """Append one expense row to the CSV file."""
    ensure_data_file()
    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(expense)


def read_date(prompt: str = "Date (YYYY-MM-DD, press Enter for today): ") -> str:
    """Read a valid YYYY-MM-DD date."""
    while True:
        value = input(prompt).strip()
        if not value:
            value = datetime.today().strftime("%Y-%m-%d")
        try:
            parsed = datetime.strptime(value, "%Y-%m-%d")
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD, for example 2026-10-24.")


def read_amount() -> str:
    """Read a non-negative amount and store it with two decimal places."""
    while True:
        value = input("Amount: ").strip()
        try:
            amount = float(value)
        except ValueError:
            print("Invalid amount. Please enter a number, such as 120.50.")
            continue
        if amount < 0:
            print("Amount cannot be negative. Please try again.")
            continue
        return f"{amount:.2f}"


def read_required_text(prompt: str) -> str:
    """Read non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def print_expenses(rows: list[dict[str, str]]) -> None:
    """Display expenses in a readable table."""
    if not rows:
        print("No expenses found.")
        return

    print("\n" + "-" * 78)
    print(f"{'Date':<12} {'Category':<14} {'Description':<30} {'Amount':>12}")
    print("-" * 78)
    for row in rows:
        print(
            f"{row.get('date', ''):<12} "
            f"{row.get('category', '')[:14]:<14} "
            f"{row.get('description', '')[:30]:<30} "
            f"{float(row.get('amount', 0)) :>12.2f}"
        )
    print("-" * 78)
    print(f"Number of expenses: {len(rows)}")


def add_expense() -> None:
    """Collect and save a new expense."""
    print("\nADD EXPENSE")
    date = read_date()
    print("Suggested categories: " + ", ".join(DEFAULT_CATEGORIES))
    category = read_required_text("Category: ").title()
    description = read_required_text("Description: ")
    amount = read_amount()

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    }
    save_expense(expense)
    print("Expense saved successfully to expenses.csv.")


def filter_expenses() -> None:
    """Filter expenses by category or month."""
    rows = load_expenses()
    if not rows:
        print("No expenses available to filter.")
        return

    print("\nFILTER EXPENSES")
    print("1. Filter by category")
    print("2. Filter by month (YYYY-MM)")
    print("3. Back")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        category = read_required_text("Enter category: ").casefold()
        filtered = [row for row in rows if row.get("category", "").casefold() == category]
        print_expenses(filtered)
    elif choice == "2":
        while True:
            month = input("Enter month (YYYY-MM): ").strip()
            try:
                datetime.strptime(month, "%Y-%m")
                break
            except ValueError:
                print("Invalid month. Use YYYY-MM, for example 2026-10.")
        filtered = [row for row in rows if row.get("date", "")[:7] == month]
        print_expenses(filtered)
    elif choice == "3":
        return
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


def show_summary() -> None:
    """Display totals per category, grand total, and largest expense."""
    rows = load_expenses()
    if not rows:
        print("No expenses available for a summary.")
        return

    totals: dict[str, float] = {}
    for row in rows:
        category = row.get("category", "Other")
        try:
            amount = float(row.get("amount", "0"))
        except ValueError:
            continue
        totals[category] = totals.get(category, 0.0) + amount

    print("\nSPENDING SUMMARY")
    print("-" * 36)
    for category, total in sorted(totals.items()):
        print(f"{category:<20} {total:>12.2f}")
    grand_total = sum(totals.values())
    largest = max(rows, key=lambda row: float(row.get("amount", "0")))
    print("-" * 36)
    print(f"{'Grand total':<20} {grand_total:>12.2f}")
    print(
        f"Largest expense: {largest.get('description', '')} "
        f"({largest.get('category', '')}) - {float(largest.get('amount', '0')):.2f}"
    )


def main() -> None:
    """Run the menu until the user chooses to quit."""
    ensure_data_file()
    print("=" * 48)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 48)

    while True:
        print("\nMAIN MENU")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Filter expenses")
        print("4. Summary")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            print_expenses(load_expenses())
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Your expenses are saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
