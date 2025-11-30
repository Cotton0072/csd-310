# movies_queries.py
# Will Cotton
# Module 7 Assignment - Movies Queries

import mysql.connector

def connect_db():
    """Connect to the MySQL movies database."""
    return mysql.connector.connect(
        user="root",
        password="Barricade1985!",
        host="localhost",
        database="movies"
    )

def show_query_results(cursor, query, description):
    """Run query and print formatted results with description."""
    cursor.execute(query)
    results = cursor.fetchall()
    print("\n-- {} --".format(description))
    for row in results:
        print(row)

def main():
    db = connect_db()
    cursor = db.cursor()

    # Query 1: Select all fields from studio
    query1 = "SELECT * FROM studio;"
    show_query_results(cursor, query1, "DISPLAYING Studio Records")

    # Query 2: Select all fields from genre
    query2 = "SELECT * FROM genre;"
    show_query_results(cursor, query2, "DISPLAYING Genre Records")

    # Query 3: Select movie names with runtime < 120 minutes
    query3 = "SELECT film_name FROM film WHERE film_runtime < 120;"
    show_query_results(cursor, query3, "DISPLAYING Films with Runtime Less Than 2 Hours")

    # Query 4: List film names and directors grouped by director
    query4 = "SELECT film_name, film_director FROM film ORDER BY film_director;"
    show_query_results(cursor, query4, "DISPLAYING Films Grouped by Director")

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
