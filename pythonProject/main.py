from pip._vendor.distlib.compat import raw_input

from AccessDataBase import AccessDatabase
from Book import Book


class Library():
    def __init__(self):
        self.login = "login"


class User:
    def __init__(self, login):
        self.login = login
        self.isConnected = False

    def giveLogin(self):
        mylogin = raw_input("Entrez votre login : ")
        self.login = mylogin

    def showBook(self):
        listBook = self.database.retrieveBookLibrary()
        print("Voici la liste des livres: ")
        for book in listBook:
            print(book.name + " : " + book.author)
        self.action()

    def authenticate(self):

        self.giveLogin()

        if dataBase.retrieveLoginUser(self.login):
            self.isConnected = True
            print("true")
            return True

        retryWord = raw_input("Mauvais login. Voulez-vous réessayer? : y pour oui ")

        if retryWord != 'y':
            return False

        return self.authenticate()



class FinalUserGenerator():
    def __init__(self, user,database):
        self.user = user

        self.role = ""

        self.finalUser = {
            "library": Librarian(self.user.login,database),
            "member": Guest(self.user.login,database),
            "guest": Member(self.user.login,database),
        }

    def GenerateFinalUser(self, role):
        return self.finalUser[role]


class Librarian(User):
    def __init__(self, login,database):
        self.database=database
        self.login = login
        self.role = dataBase.retrieveRoleUser(login)

    def action(self):
        choice = raw_input("Si vous voulez voir les livres tapez 1, tapez autre chose pour ajouter un livre.")

        if choice == "1":
            return self.showBook()

        return self.addBook()

    def addBook(self):
        bookName = raw_input("Sélectionez un nom : ")
        authorName = raw_input("Sélectionez un autheur : ")
        newBook = Book(bookName, authorName)
        self.database.addBookLibrary(newBook)
        response = raw_input("Livre ajouté. Voulez-vous continuer? y pour oui : ")
        if response == 'y':
            self.addBook()

class Guest(User):
    def __init__(self, login, database):
        self.database = database
        self.login = login
        self.role = dataBase.retrieveRoleUser(login)
        self.nbBorrowBook = 0

    def action(self):
        listBook = self.database.retrieveBookLibrary()
        print("Voici la liste des livres: ")
        for book in listBook:
            print(book.name + " : " + book.author)

class Member(User):
    def __init__(self, login,database):
        self.database = database
        self.login = login
        self.role = dataBase.retrieveRoleUser(login)
        self.nbBookBorrow = 0

    def action(self):

        choice = raw_input("Si vous voulez voir les livres tapez 1, tapez autre chose pour emprunter.")

        if choice == "1":
            return self.showBook()

        return self.borrowBook()




    def borrowBook(self):
        if self.nbBookBorrow > 3:
            print("Vous avez emprunté le nombre maximum de livre: ")

        listBook = self.database.retrieveBookLibrary()
        print("Voici la liste des livres: ")
        for book in listBook:
            print(book.name + " : " + book.author)

        response = raw_input("Saisissez le nom du livre que vous voulez emprunter : ")
        print("Vous avez emprunté : " + response)

        responseContinue = raw_input("Voulez-vous continuer? y pour oui : ")
        if responseContinue == 'y':
            self.nbBookBorrow = self.nbBookBorrow + 1

            self.action()


if __name__ == '__main__':

    dataBase = AccessDatabase("Books", "Users")
    userTest = User("")

    if userTest.authenticate():
        print("Connected")
    else:
        print("not Connected")

    finalUserGenerator = FinalUserGenerator(userTest,dataBase)
    finalUser = finalUserGenerator.GenerateFinalUser(dataBase.retrieveRoleUser(userTest.login))


    finalUser.action()