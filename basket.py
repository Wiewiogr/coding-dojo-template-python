import sets

#Nothing works!!!!!!
#We started changing everything in last minutes

class Basket:
    def __init__(self):
        self.pricePerBook = 100
        self.discounts = {0:0, 1:1.0, 2:0.95, 3:0.9, 4:0.8, 5:0.75}
        self.books = {}
        #self.differentBooks = [sets.Set()]
        #self.priceWithoutDiscount = 0

    def addBook(self, name):
        if name in self.books:
            self.books[name] += 1
        else:
            self.books[name] = 1

    def getPrice(self):
        price = 0
        bookShelves = []
        for book in self.books:
            bookCount = self.books[book]
            for i in range(bookCount):
                if len(bookShelves) == 0:
                    bookShelves.append([book])
                else:
                    for shelf in bookShelves:
                        if book in shelf:
                            continue
                        else:
                            shelf.append(book)
        return price

