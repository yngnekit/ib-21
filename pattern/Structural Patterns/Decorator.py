class Coffee:
    def get_cost(self):
        return 5

    def get_description(self):
        return "Basic Coffee"

class CoffeeDecorator:
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_description(self):
        return self.decorated_coffee.get_description()

class MilkDecorator(CoffeeDecorator):
    def __init__(self, decorated_coffee):
        super().__init__(decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 1

    def get_description(self):
        return self.decorated_coffee.get_description() + ", Milk"

class ChocolateDecorator(CoffeeDecorator):
    def __init__(self, decorated_coffee):
        super().__init__(decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 2

    def get_description(self):
        return self.decorated_coffee.get_description() + ", Chocolate"

class CaramelDecorator(CoffeeDecorator):
    def __init__(self, decorated_coffee):
        super().__init__(decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 3

    def get_description(self):
        return self.decorated_coffee.get_description() + ", Caramel"

basic_coffee = Coffee()
print(basic_coffee.get_description())
print(basic_coffee.get_cost())

milk_coffee = MilkDecorator(basic_coffee)
print(milk_coffee.get_description())
print(milk_coffee.get_cost())

chocolate_milk_coffee = ChocolateDecorator(milk_coffee)
print(chocolate_milk_coffee.get_description())
print(chocolate_milk_coffee.get_cost())

caramel_chocolate_milk_coffee = CaramelDecorator(
    chocolate_milk_coffee)
print(caramel_chocolate_milk_coffee.get_description())
print(caramel_chocolate_milk_coffee.get_cost())