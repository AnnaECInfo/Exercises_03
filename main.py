#exercise 1
def count_vowels(text):
    if text is str:
        vowel_number = 0
        vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
        for i in text:
            if i in vowels:
                vowel_number = vowel_number + 1
        return int(vowel_number)
    else:
        return 42

#exercise 2
def hamming(text1, text2):
    if len(text1) is not len(text2):
        return 0
    else:
        distance = 0
        for i in range(len(text1)):
            if text1[i] != text2[i]:
                distance = distance + 1
        return distance

#exercise 3
class Vehicle():
    def __init__(self, color, fuel_type):
        self.my_color = color
        self.my_fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        Vehicle.__init__(self, color, fuel_type)
        self.doors = doors
    def __str__(self):
        return f"Color: {self.my_color}, Fuel Type {self.my_fuel_type}, Doors: {self.doors}"

class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        Vehicle.__init__(self, color, fuel_type)
        self.passengers = passengers
    def __str__(self):
        return f"Color: {self.my_color}, Fuel Type {self.my_fuel_type}, Passengers: {self.passengers}"

#exercise 4
class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def __str__(self):
        return f"{self.name}, {self.author}"

#exercise 5
class BookShelf():
    def __init__(self, definite_book_list: []):
        self.definite_book_list = definite_book_list
    def add_book_list(self, books):
        for i in books:
            if isinstance(i, Book) and i not in self.definite_book_list:
                self.definite_book_list.append(i)
    def books_by_author(self, author):
        author_book_list = []
        for i in self.definite_book_list:
            if i.author == author:
                author_book_list.append(i)
        return author_book_list
    def get_books(self):
        books = []
        if self.definite_book_list:
            for i in self.definite_book_list:
                books.append(i.name)
            return books
        else:
            return []
    def clear_shelf(self):
        self.definite_book_list = []