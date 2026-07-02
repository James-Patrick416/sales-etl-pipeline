import sqlite3
import matplotlib.pyplot as plt


def generate_chart(database_file):
    connection = sqlite3.connect(database_file)

    query = """
        SELECT Product, SUM(Total) AS Revenue
        FROM sales
        GROUP BY Product
        ORDER BY Revenue DESC
    """

    data = connection.execute(query).fetchall()

    products = [row[0] for row in data]
    revenue = [row[1] for row in data]

    plt.figure(figsize=(8, 5))
    plt.bar(products, revenue)

    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("reports/charts/revenue_by_product.png")

    plt.close()
    connection.close()

    print("Chart generated successfully.")