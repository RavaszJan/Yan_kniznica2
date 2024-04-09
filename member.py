

class Member:
    def __init__(self,id,first_name,last_name,email,registration_date):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.registration_date=registration_date

    @staticmethod
    def vloz_do_db(cursor):
        print("Vlozte first_name clena: ")
        first_name = input()
        print("Vlozte last_name clena: ")
        last_name = input()
        print("Vloz email clena:")
        email=input()
        print("Vloz registration_date:")
        registrtion_date=input()

        cursor.execute("INSERT INTO members (first_name,last_name,email,registration_date) VALUES (%s, %s,%s,%s)", (first_name,last_name,email,registrtion_date))