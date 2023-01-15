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

car1 = Car("X","2022", "Tesla", "2.0", "black", "23000")
car2 = Car("Corsa","2000", "Opel", "1.2", "blue", "10000")

print(car1.price)
print(car2.engine_capacity)
print(car1.engine_capacity)
print(car2.model)
print(car1.colour)

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