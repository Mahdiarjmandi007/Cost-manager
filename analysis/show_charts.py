import matplotlib.pyplot as plt
from database.database import Connection


def plot_expense_chart(date_pattern,title):
    connection=Connection()
    cursor=connection.cursor()
    cursor.execute("""
    SELECT date, SUM(amount)
    FROM costs
    WHERE date LIKE ?
    GROUP BY date
    ORDER BY date
    """, (date_pattern,))

    result = cursor.fetchall()
    connection.close()
    labels = []
    values = []

    for row in result:
        labels.append(row[0])
        values.append(row[1])   

    plt.figure(figsize=(10, 5))

    plt.plot(
        labels,
        values,
        marker="o"
    )

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Amount")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()
    input("\nPress enter to return: ")

