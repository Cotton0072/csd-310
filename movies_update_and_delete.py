import mysql.connector

def connect_db():
    return mysql.connector.connect(
        user="root",
        password="Barricade1985!",
        host="localhost",
        database="movies"
    )

def show_films(cursor, label):
    # Join film with genre and studio to display complete info
    query = """
        SELECT film.film_name, film.film_director, film.film_runtime, film.film_releaseDate,
               genre.genre_name, studio.studio_name
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    cursor.execute(query)
    films = cursor.fetchall()
    print("\n-- {} --".format(label))
    for film in films:
        print(film)

def main():
    db = connect_db()
    cursor = db.cursor()

    # 1. Show films before changes
    show_films(cursor, "DISPLAYING FILMS BEFORE CHANGES")

    # 2. Insert a new film (Jurassic World) with year-only release date
    cursor.execute("""
        INSERT INTO film (film_name, film_director, film_runtime, film_releaseDate, studio_id, genre_id)
        VALUES ('Jurassic World', 'Colin Trevorrow', 124, '2015', 1, 2);
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # 3. Update Alien to Horror
    cursor.execute("""
        UPDATE film
        SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
        WHERE film_name = 'Alien';
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATING ALIEN TO HORROR")

    # 4. Delete Gladiator
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator';")
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETING GLADIATOR")

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()

