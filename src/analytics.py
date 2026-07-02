import sqlite3


def run_analytics(database_file):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    print("\n------ Sales Analytics ------")

    # Total Revenue
    cursor.execute("SELECT SUM(Total) FROM sales")
    total_revenue = cursor.fetchone()[0]
    print(f"Total Revenue: ${total_revenue}")

    # Number of Orders
    cursor.execute("SELECT COUNT(*) FROM sales")
    orders = cursor.fetchone()[0]
    print(f"Total Orders: {orders}")

    # Average Order Value
    cursor.execute("SELECT AVG(Total) FROM sales")
    average = cursor.fetchone()[0]
    print(f"Average Order Value: ${average:.2f}")

    # Highest Value Order
    cursor.execute("""
        SELECT Customer, Total
        FROM sales
        ORDER BY Total DESC
        LIMIT 1
    """)

    customer, total = cursor.fetchone()
    print(f"Highest Order: {customer} (${total})")

    connection.close()