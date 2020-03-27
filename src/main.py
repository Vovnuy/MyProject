class NotEnoughFunds(Exception):
    pass

class CarShop:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.fleet = []

    def payday(self, money):
        self.balance -= money

    def add_funds(self, amount):
        self.balance += amount

    def buy_car(self, car):
        if self.balance >= car.cost:
            self.balance -= car.cost
            self.fleet.append(car)
            print(f"{self.name} bought a new car{car}")
        else:
            raise NotEnoughFunds()

class BMW_M5_E60:
    def __init__(self, name, cost, prod_year, hp):
        self.name = name
        self.cost = cost
        self.prod_year = prod_year
        self.hp = hp

    def __str__(self):
        return f" {self.name} {self.prod_year} {self.hp}hp"

class BMW_M5_F10:
    def __init__(self, name, cost, prod_year, hp):
        self.name = name
        self.cost = cost
        self.prod_year = prod_year
        self.hp = hp

    def __str__(self):
        return f" {self.name} {self.prod_year} {self.hp}hp"

class BMW_5_GT:
    def __init__(self, name, cost, prod_year, hp):
        self.name = name
        self.cost = cost
        self.prod_year = prod_year
        self.hp = hp

    def __str__(self):
        return f" {self.name} {self.prod_year} {self.hp}hp"

class BMW_5_G30:
    def __init__(self, name, cost, prod_year, hp):
        self.name = name
        self.cost = cost
        self.prod_year = prod_year
        self.hp = hp

    def __str__(self):
        return f" {self.name} {self.prod_year} {self.hp}hp"

class Manager:
    def __init__(self, name, lastname, age, salary, experience):
        self.experience = experience
        if self.experience >=6:
            self.name = name
            self.lastname = lastname
            self.age = age
            self.salary = salary
            self.begin_to_work = True
        else:
            self.begin_to_work = False

class Consultant:
    def __init__(self, name, lastname, age, salary, experience):
        self.experience = experience
        if self.experience >= 2:
            self.name = name
            self.lastname = lastname
            self.age = age
            self.salary = salary
            self.begin_to_work = True
        else:
            self.begin_to_work = False

class Customer:
    def __init__(self, name, lastname, age, balance):
            self.balance = balance
            self.name = name
            self.lastname = lastname
            self.age = age

    def customer_buy_car(self, BMW_5_G30):
        if self.balance >= BMW_5_G30.cost:
            self.balance -= BMW_5_G30.cost
            self.customer_buy_car = True
        else:
            self.customer_buy_car = False

def main():
    # Назва компанії
    carshop = CarShop("BMW")
    print(carshop)
    # Назва компанії
    # Закуп машин
    carshop.add_funds(20000000)
    print(f'{carshop.balance} весь баланс')
    bmw_m5_e60 = BMW_M5_E60("BMW M5 E60", 35000, 2010, 450)
    bmw_m5_f10 = BMW_M5_F10("BMW M5 F10", 45000, 2016, 560)
    bmw_5_gt = BMW_5_GT("BMW 5 GT", 35000, 2017, 240)
    bmw_5_g30 = BMW_5_G30("BMW 5 G30", 45000, 2019, 252)
    first_car = bmw_m5_e60
    carshop.buy_car(first_car)
    second_car = bmw_m5_f10
    carshop.buy_car(second_car)
    third_car = bmw_5_gt
    carshop.buy_car(third_car)
    four_car = bmw_5_g30
    carshop.buy_car(four_car)
    print(f'{carshop.balance} весь баланс')
    # Закуп машин
    # Менеджер
    manager = Manager('Emma', 'Smith', 34, 6000, 6)
    if manager.begin_to_work == True:
        print(f'Менеджер:{manager.name} {manager.lastname},{manager.age} була прийнята на роботу ')
        carshop.payday(manager.salary)
    else:
        print("Менеджер має не достатньо досвіду для цієї роботи")
    # Менеджер
    # Консультант
    consultant = Consultant('Michael', 'Murphy', 41, 1500, 2)
    if manager.begin_to_work == True:
        print(f'Консультант:{consultant.name} {consultant.lastname},{consultant.age} був прийнятий на роботу ')
        carshop.payday(consultant.salary)
    else:
        print("Консультант має не достатньо досвіду для цієї роботи")
    print(f'{carshop.balance} весь баланс')
    # Консультант
    # Покупець
    customer = Customer('Tim','Perry', 21, 45000)
    if  customer.customer_buy_car == True:
        print(f"{customer.name} {customer.lastname} купив нову машину{car}")
        carshop.add_funds(bmw_5_g30.cost)
    else:
        print(f"У {customer.name} {customer.lastname} недостатньо грошей")
    # Покупець
    print(f'{carshop.balance} весь баланс')
main()