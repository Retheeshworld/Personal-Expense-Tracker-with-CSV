"""Automated tests for the expense tracker."""

import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import expense_tracker as app


class ExpenseTrackerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_file = app.DATA_FILE
        app.DATA_FILE = Path(self.temp_dir.name) / "expenses.csv"

    def tearDown(self):
        app.DATA_FILE = self.original_file
        self.temp_dir.cleanup()

    def test_missing_file_is_created_with_header(self):
        app.ensure_data_file()
        with app.DATA_FILE.open(newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            self.assertEqual(next(reader), app.FIELDS)

    def test_save_and_load_expense(self):
        expense = {
            "date": "2026-10-04",
            "category": "Food",
            "description": "Lunch",
            "amount": "120.50",
        }
        app.save_expense(expense)
        self.assertEqual(app.load_expenses(), [expense])

    def test_month_filter_key_format_is_supported(self):
        rows = [
            {"date": "2026-10-04", "category": "Food", "description": "Lunch", "amount": "120.50"},
            {"date": "2026-09-04", "category": "Travel", "description": "Bus", "amount": "45.00"},
        ]
        self.assertEqual([r for r in rows if r["date"][:7] == "2026-10"], [rows[0]])

    def test_read_amount_rejects_invalid_and_negative_values(self):
        with patch("builtins.input", side_effect=["abc", "-4", "25.5"]):
            with patch("builtins.print"):
                self.assertEqual(app.read_amount(), "25.50")

    def test_read_date_retries_invalid_date(self):
        with patch("builtins.input", side_effect=["2026-13-45", "2026-10-24"]):
            with patch("builtins.print"):
                self.assertEqual(app.read_date(), "2026-10-24")


if __name__ == "__main__":
    unittest.main()
