import datetime

class StockedItem:
    def __init__(self, title:str):
        self._title = title
        self._on_loan = False
        self._DateAcquired = datetime.datetime.now()

class Book(StockedItem):
    def __init__(self, title:str, author:str, isbn:int):
        super().__init__(title)
        self._author = author
        self._isbn = isbn
    
    def __repr__(self):
        return [self._title, self._author, self._isbn, self._on_loan, self._DateAcquired]
    
    def __str__(self):
        return f"{self._title} by {self._author}, ISBN {str(self._isbn)}, on loan: {str(self._on_loan)}"

    def loan(self):
        if self._on_loan == True:
            raise ValueError # already on loan
        else:
            self._on_loan = True
        return 0
    
    def return_Book(self):
        if self._on_loan == False:
            raise ValueError # already not on loan
        else:
            self._on_loan = False
        return 0

class Disk(StockedItem):
    def __init__(self, title:str, artist:str, playing_time:int):
        super().__init__(title)
        self._artist = artist
        self._playing_time = playing_time
    
    def __repr__(self):
        return [self._title, self._artist, self._playing_time, self._on_loan, self._DateAcquired]
    
    def __str__(self):
        return f"{self._title} by {self._artist}, Length {str(self._playing_time)}, on loan: {str(self._on_loan)}"

    def loan(self):
        if self._on_loan == True:
            raise ValueError # already on loan
        else:
            self._on_loan == True
        return 0
    
    def return_disk(self):
        if self._on_loan == False:
            raise ValueError # already not on loan
        else:
            self._on_loan == False
        return 0

def test_library():
    trauma = Book("Things Fall Apart", "Chinua Achebe", "9780435272463")
    trauma.loan()
    print(trauma)
    trauma.return_Book()
    nugget = Disk("Scarlet Fire", "Otis Macdonald", "9008")
    print(trauma)
    print(nugget)

if __name__ == "__main__":
    test_library()