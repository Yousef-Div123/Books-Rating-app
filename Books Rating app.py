#Your code below this line

class Book():
    def __init__(self, ISPN, bookTitle, averageRating = 0, numbereOfRaters = 0):
        self._ISPN = ISPN
        self._bookTitle = bookTitle
        # make sure that number of raters and average rating is saved as integer
        self._numbereOfRaters = int(numbereOfRaters)
        self._averageRating = int(averageRating)

    # getter methods
    def getAvgRating(self):
        return self._averageRating
    
    def getBookISPN(self):
        return self._ISPN
    
    def getBookTitle(self):
        return self._bookTitle
    
    def getNumberOfRaters(self):
        return self._numbereOfRaters
    
    # This is a method which get a rating then add it to the average rating and increase the number of raters
    def addRating(self, bookRating):
        # calculating the new average
        self._averageRating = round((self._averageRating*self._numbereOfRaters + bookRating)/(self._numbereOfRaters + 1), 1)
        self._numbereOfRaters += 1

    def toString(self):
        # I put \n in the end of the string because write function doesn't add it automaticaly like print
        return f"{self._ISPN},{self._bookTitle},{self._averageRating},{self._numbereOfRaters}\n" 


def booksFromFile(bookFile):
    file = open(bookFile, 'r')
    # getting a list of all the lines in the file
    lines = file.readlines()

    # this is the list of the books that I am going to return
    books = []

    for line in lines:
        line = line.rstrip() # removing \n from the end of the line
        line = line.split(',')# getting the indivdual data in the list
        if line[0] != 'ISBN': # this if statment to skip the first line as it is the line of labels for the data in the file
            book = Book(line[0], line[1], line[2], line[3]) # the data in the file is in the following order (ISBN,Book-Title,Total-Rating,Total-Raters)
            books.append(book)

    file.close()

    return books

def rateBooks(bookList):
    # giving an intial value for id so the loop start
    id = ' '
    while id != '':
        print("The books available for rating are:")
        i = 1 # i is for the book id which should start from 1
        for book in bookList:
            print(f"book id: {i} {book.getBookTitle()} Average rating: {book.getAvgRating()} from: {book.getNumberOfRaters()} user(s).")
            i += 1
        id = input('Enter book id to rate or press ENTER to exit: ')
        # to determain if the book is a positive intiger
        if id.isdigit():
            id = int(id)
            # i here should be the number of books avilable
            if i >= id >= 1:
                # now I am asking the user for a valid rating
                validRating = False
                while not validRating: 
                    rating = input('Enter your rating 0-5: ') 
                    if rating.isdigit():
                        rating = int(rating)
                        if 5>= rating >= 0:
                            # ending the validation loop for rating
                            validRating = True
                        else:
                            print("rating must be between 0 and 5")
                    elif '.' in rating: # this make sure that the rating is intiger 
                        print("rating must be an integer between 0 and 5")
                    else:
                        print("rating must be between 0 and 5")
                # reducing the id by 1 because the index of the books in the list starts from 0
                id -= 1
                # getting the specfic book
                book = bookList[id]
                book.addRating(rating)

            else:
                print('You did not enter correct book id')

        elif id != '':
            print('You did not enter correct book id')
            

    # after the user end the programm I return the modifaied book list to save in books.txt file
    return bookList
    
def writeRatingsToFile(bookList, fileName):  
    file = open(fileName, 'w')
    file.write("ISBN,Book-Title,Total-Rating,Total-Raters\n") # this is for the labels line
    for book in bookList: # looping over all the books
        file.write(book.toString())

    file.close()


def main():
    books = booksFromFile('books.txt') # getting the data from the file and saving it as classes
    print('Welcome to the book rating app!')
    books = rateBooks(books) # the main loop of the program
    writeRatingsToFile(books, 'books.txt') # saving the acquired data
    print("Thanks for using the book rating app")

main()
