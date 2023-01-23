# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Классы. Объекты. Часть 1

# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить# в полях класса: 
# название модели, 
# год выпуска, 
# производителя, 
# объем двигателя, 
# цвет машины, 
# цену. 
# Реализуйте методы класса для ввода данных, вывода данных, 
# реализуйте доступ к отдельным полям через методы класса.
 
class Car:
    def __init__(self, model, year, brand, engine_capacity, сolour, price):
        self.model = model
        self.year = year
        self.brand = brand
        self.engine_capacity = engine_capacity
        self.colour = сolour
        self.price = price

car1 = Car("X","2022", "Tesla", "Electric", "black", "23000")
car2 = Car("Corsa","2000", "Opel", "1.2", "blue", "10000")

print(car1.price)
print(car2.engine_capacity)
print(car1.engine_capacity)
print(car2.model)

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: 
# название книги,  
# год выпуска, 
# издателя,
# жанр, 
# автора, 
# цену. 
# Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

book1 = Book("Книга1","2022", "Издательство1", "Жанр1", "Автор1", "23")
book2 = Book("Книга2","2000", "Издательство2", "Жанр2", "Автор2", "10")

print(book1.price)
print(book2.publisher)
print(book1.publisher)
print(book2.author)

# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: 
# название стадиона, 
# дату открытия, 
# страну,
# город, 
# вместимость. 
# Реализуйте методы класса для ввода данных, вывода данных, 
# реализуйте доступ к отдельным полям через методы класса.

class Stadium:
    def __init__(self, title, year, country, town, capacity):
        self.title = title
        self.year = year
        self.country = country
        self.town = town
        self.capacity = capacity
        
stadium1 = Stadium("Уэмбли","2007", "Великобритания", "Лондон", "90 000")
stadium2 = Stadium("Днепр Арена","2008", "Украина", "Днепр", "34 000")

print(stadium1.title)
print(stadium2.capacity)
print(stadium1.capacity)
print(stadium2.town)