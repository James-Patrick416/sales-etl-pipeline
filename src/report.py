import sqlite3
from datetime import datetime


def generate_report(database_file):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Summary statistics
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

    # Get every sale
    cursor.execute("""
        SELECT OrderID, Customer, Product, Quantity, Price, Total
        FROM sales
    """)
    rows = cursor.fetchall()

    table_rows = ""

    for row in rows:
        table_rows += f"""
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
            <td>${row[4]}</td>
            <td>${row[5]}</td>
        </tr>
        """

    html = f"""
<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<title>Sales Dashboard</title>

<style>

body {{
    font-family: Arial, sans-serif;
    background:#f4f4f4;
    margin:40px;
}}

.container {{
    max-width:1000px;
    margin:auto;
    background:white;
    padding:30px;
    border-radius:10px;
}}

.card {{
    background:#1f6feb;
    color:white;
    padding:15px;
    border-radius:8px;
    margin-bottom:15px;
}}

table {{
    width:100%;
    border-collapse:collapse;
}}

th, td {{
    border:1px solid #ddd;
    padding:10px;
}}

th {{
    background:#1f6feb;
    color:white;
}}

tr:nth-child(even) {{
    background:#f7f7f7;
}}

img {{
    width:100%;
    margin-top:20px;
}}

</style>

</head>

<body>

<div class="container">

<h1>Sales ETL Dashboard</h1>

<p>Generated: {datetime.now()}</p>

<div class="card">
<h2>Total Revenue: ${revenue}</h2>
<h2>Total Orders: {orders}</h2>
<h2>Average Order Value: ${average:.2f}</h2>
<h2>Highest Order: {customer} (${total})</h2>
</div>

<h2>Revenue by Product</h2>

<img src="charts/revenue_by_product.png">

<h2>Sales Records</h2>

<table>

<tr>
<th>Order ID</th>
<th>Customer</th>
<th>Product</th>
<th>Quantity</th>
<th>Price</th>
<th>Total</th>
</tr>

{table_rows}

</table>

</div>

</body>
</html>
"""

    with open("reports/report.html", "w", encoding="utf-8") as file:
        file.write(html)

    connection.close()

    print("Professional HTML report generated.")