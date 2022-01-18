from tkinter import CENTER


class Library:
    def __init__(self,listOfBooks):
        self.books= listOfBooks
        
    def displayAvailableBooks(self):
        print('Books present in this library are: ')
        for book in self.books:
            print("-->"+book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} book")
            self.books.remove(bookName)
            return True
        else:
            print("sorry, This book is either not available or has been issued to somebody . please wait until the book is returned")
            return False
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!")

class Student:

    def requestBook(self):
        self.Book=input('enter the name of the book you want to borrow: ')
        return self.Book

    def returnBook(self):
        self.Book=input('enter the name of the book you want to return: ')
        return self.Book
 

if __name__=="__main__":
    centralLibrary=Library(["Algorithms","django","python books","dsa"])
    student=Student()
    centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg='''=====wellcome to central library=====
        please choose an option:
        1.List all the books
        2.Request a book
        3.Add/Return a book
        4.Exit the library
        '''
        print(welcomeMsg)
        a=int(input("enter your choice:"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            exit()
        else:
            print("Invalid Choice")

        


