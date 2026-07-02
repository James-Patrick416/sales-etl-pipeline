import sqlite3


def generate_report(database_file):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(Total) FROM sales")
    revenue = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM sales")
    orders = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(Total) FROM sales")
    average = cursor.fetchone()[0]

    cursor.execute("""
        SELECT Customer, Total
        FROM sales
        ORDER BY Total DESC
        LIMIT 1
    """)
    customer, total = cursor.fetchone()

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sales Report</title>
    </head>
    <body>
        <h1>Sales ETL Report</h1>

        <p><strong>Total Revenue:</strong> ${revenue}</p>
        <p><strong>Total Orders:</strong> {orders}</p>
        <p><strong>Average Order Value:</strong> ${average:.2f}</p>
        <p><strong>Highest Order:</strong> {customer} (${total})</p>

    </body>
    </html>
    """

    with open("reports/report.html", "w") as file:
        file.write(html)

    connection.close()

    print("HTML report generated successfully.")