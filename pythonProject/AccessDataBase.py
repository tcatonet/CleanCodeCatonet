

import pandas as pd

from Book import Book


class DatabaseName():
    def __init__(self, databaseName):
        self.databaseName = databaseName


class AccessDatabase():
    def __init__(self, bookDatabaseName, userDatabaseName):
        self.bookDatabaseName = DatabaseName(bookDatabaseName)
        self.userDatabaseName = DatabaseName(userDatabaseName)

    def addBookLibrary(self, book):
        FILE = self.bookDatabaseName.databaseName

        with open(FILE, 'r+') as readWrite:
            allLines = readWrite.readlines()
            info = ";;" + book.name + "!!" + book.author +"0"
            readWrite.write(info)


    def addBookLibrary(self, book):
        FILE = self.bookDatabaseName.databaseName

        with open(FILE, 'r+') as readWrite:
            allLines = readWrite.readlines()
            info = ";;" + book.name + "!!" + book.author
            readWrite.write(info)



    def retrieveBookLibrary(self):
        FILE = self.bookDatabaseName.databaseName

        with open(FILE, 'r+') as readWrite:
            allLines = readWrite.readlines()
            tabBook = allLines[0].split(';;')

            listBook = []
            for x in tabBook:
                tab = x.split('!!')
                name = tab[0]
                autheur = tab[1]
                book = Book(name,autheur)
                listBook.append(book)

        return listBook

    def retrieveLoginUser(self, login):
        FILE = self.userDatabaseName.databaseName

        with open(FILE, 'r+') as readWrite:
            allLines = readWrite.readlines()
            tabUser = allLines[0].split(';;')

        for x in tabUser:
            tab = x.split('!!')
            name = tab[0]
            role = tab[1]

            if name == login:
                return True

        return False

    def retrieveRoleUser(self, login):
        FILE = self.userDatabaseName.databaseName

        with open(FILE, 'r+') as readWrite:
            allLines = readWrite.readlines()
            tabUser = allLines[0].split(';;')

        for x in tabUser:
            tab = x.split('!!')
            name = tab[0]
            role = tab[1]

            if name == login:
                return role
