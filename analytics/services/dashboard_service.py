from django.db import connection


def get_dashboard_stats():
    with connection.cursor() as cursor:

        cursor.execute("SELECT COUNT(*) FROM orders")
        total_orders = cursor.fetchone()[0]

        cursor.execute("""
            SELECT SUM(quantity * unit_price)
            FROM orders o
            JOIN products p
            ON o.product_id = p.product_id
        """)
        total_revenue = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM customers")
        total_customers = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM products")
        total_products = cursor.fetchone()[0]

    return {
        "orders": total_orders,
        "revenue": round(float(total_revenue), 2),
        "customers": total_customers,
        "products": total_products,
    }