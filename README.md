# Cost Manager CLI

A simple command-line expense manager built with **Python** and **SQLite**.

This project was developed as part of my internship training to practice Python, SQL, SQLite, CRUD operations, CLI development, and basic data analysis.

---

## Features

- Add, edit, and delete expenses
- View recent expenses
- Add and manage categories
- Monthly reports
- Yearly reports
- Category analysis
- All-time statistics
- Expense visualization with Matplotlib
- SQLite database for persistent storage

---

## Tech Stack

- Python 3.11
- SQLite
- Matplotlib
- Git / GitHub

---

## Project Structure

```text
Cost-manager/
│
├── analysis/
│   ├── menu.py
│   ├── reports.py
│   └── charts.py
│
├── cli/
│   ├── add_expense_menu.py
│   ├── category_menu.py
│   ├── delete_expense.py
│   ├── edit_expense.py
│   ├── menu.py
│   └── view.py
│
├── database/
│   └── database.py
│
├── data/
│   └── database.db
│
├── main.py
├── .gitignore
└── README.md
```

---

## Database

The application uses SQLite with two main tables:

### `costs`

| Column | Description |
|---|---|
| `id` | Expense ID |
| `amount` | Expense amount |
| `category_id` | Category reference |
| `date` | Expense date |
| `description` | Optional description |

### `categories`

| Column | Description |
|---|---|
| `id` | Category ID |
| `name` | Category name |

Expenses are connected to categories using `category_id`.

---

## Analysis

The application provides:

- **Monthly reports**
  - Total expenses
  - Average expense
  - Number of expenses
  - Daily expense chart

- **Yearly reports**
  - Total expenses
  - Average expense
  - Number of expenses
  - Expense chart

- **Category analysis**
  - Monthly
  - Yearly
  - All time

Category analysis uses SQL aggregation such as:

```text
SUM()
AVG()
COUNT()
GROUP BY
ORDER BY
JOIN
```
---

## Error Handling

The application handles common CLI input errors such as:

- Invalid numeric input
- Invalid menu options
- Invalid category selection
- Empty query results

---

## Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/Cost-manager.git
cd Cost-manager
```

Install dependencies:

```bash
pip install matplotlib
```

Run the application:

```bash
python main.py
```

The required `data` directory and SQLite database are created automatically if they do not exist.


---

## Future Improvements

- Unit tests
- CSV export
- Date-range filtering

---

## License

MIT License