
def vypis_menu():
    print("1. Vyhladat podla nazvu:")
    print("2. Vyhladat podla book_id:")
    print("3. Vyhladat podla autora:")
class Book:
    def __init__(self, id, title, author_id, genre_id, isbn, publication_year, copies):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_year = publication_year
        self.copies = copies




    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2])

    @staticmethod
    def vloz_do_db(cursor, author_id, genre_id):
        print("Vlozte nazov knihy ")
        title = input()
        print("Vlozte ISBN: ")
        isbn = input()
        cursor.execute("INSERT INTO books (title, author_id, genre_id, isbn) VALUES (%s, %s, %s, %s)", (title, author_id, genre_id, isbn))

    @staticmethod
    def zobraz_knihy(cursor):
        print("-- Zoznam knih --")
        cursor.execute("SELECT book_id, title FROM books")
        books = cursor.fetchall()
        for book in books:
            print(f"ID: {book[0]}, Name: {book[1]}")

    @staticmethod
    def vymaz_knihu(cursor):
        print("Vlozte id_book: ")
        book_id = input()
        cursor.execute("DELETE FROM books WHERE book_id=%s",(book_id))
        print("Kniha bola vymazana.")
        print()
    @staticmethod
    def vyhladavanie_knih(cursor):
        while True:
            vypis_menu()
            choice=input("Vasa moznost:")
            if choice=="1":
                print("Vlozte nazov knihy: ")
                title=input()
                cursor.execute("SELECT * FROM books WHERE title=%s",(title,))
                book=cursor.fetchall()
                print(book)
            if choice=="2":
                print("Vlozte book_id:")
                book_id=input()
                cursor.execute("SELECT * FROM books WHERE book_id=%s",(book_id,))
                book1 = cursor.fetchall()
                print(book1)
            if choice == "3":
                print("Vlozte meno autora:")
                author = input()
                cursor.execute("SELECT author_id FROM authors WHERE name=%s",(author,))
                author_id=cursor.fetchall()
                author_id=author_id[0][0]
                print(author_id)

                cursor.execute("SELECT * FROM books books JOIN authors authors ON books.author_id=authors.author_id WHERE authors.author_id=%s ",(author_id,))
                book3 = cursor.fetchall()
                for book in book3:
                    print(book)



