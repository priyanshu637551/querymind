from django.db import connection


def execute_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

    if not is_safe_query(query):
        raise ValueError("Only SELECT queries are allowed.")

    return columns, rows


def is_safe_query(sql):

    sql = sql.strip().upper()

    return sql.startswith("SELECT")