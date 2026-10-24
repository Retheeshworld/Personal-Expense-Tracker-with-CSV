# Testing Guide

## Automated tests
Run:
```bash
python -m unittest -v
```

Automated tests check:
- Automatic creation of `expenses.csv` with the correct header.
- Saving and reloading an expense.
- Month filtering by the `YYYY-MM` prefix.
- Rejecting invalid and negative amounts.
- Rejecting invalid dates and prompting again.

## Manual checklist
- [ ] Add an expense with a valid date and amount.
- [ ] Press Enter for the date and confirm today's date is used.
- [ ] Enter an invalid date and confirm the app asks again.
- [ ] Enter a negative amount and confirm it is rejected.
- [ ] View all expenses in a table.
- [ ] Filter by a category.
- [ ] Filter by month such as `2026-10`.
- [ ] Confirm the summary shows category totals and a grand total.
- [ ] Confirm the largest expense is displayed.
- [ ] Quit and restart; confirm saved data remains.
- [ ] Open `expenses.csv` in a spreadsheet app and inspect its columns.

## Sample data note
The supplied CSV includes ten fictional expenses across two months, as required by the learner guide. Do not use real bank details or private financial information.
