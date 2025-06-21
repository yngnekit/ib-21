# Компоненты автомобиля
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def __str__(self):
        return self.engine_type


class Transmission:
    def __init__(self, transmission_type):
        self.transmission_type = transmission_type

    def __str__(self):
        return self.transmission_type


class Body:
    def __init__(self, body_type):
        self.body_type = body_type

    def __str__(self):
        return self.body_type


# Класс автомобиля
class Car:
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.body = None

    def set_engine(self, engine):
        self.engine = engine

    def set_transmission(self, transmission):
        self.transmission = transmission

    def set_body(self, body):
        self.body = body

    def __str__(self):
        return f"Автомобиль с {self.engine} двигателем. {self.transmission} коробкой передач. Кузов - {self.body}"


# Абстрактный строитель
class CarBuilder:
    def reset(self):
        self.car = Car()

    def build_engine(self):
        pass

    def build_transmission(self):
        pass

    def build_body(self):
        pass

    def get_car(self):
        return self.car

class SedanBuilder(CarBuilder):
    def build_engine(self):
        self.car.set_engine(Engine("1.4 л 16-кл. (98 л.с.), 5МТ"))

    def build_transmission(self):
        self.car.set_transmission(Transmission("Механической, 5-ступенчатой"))

    def build_body(self):
        self.car.set_body(Body("Седан"))


class SUVBuilder(CarBuilder):
    def build_engine(self):
        self.car.set_engine(Engine("2.5 TDI 8AT (216 л. с.)"))

    def build_transmission(self):
        self.car.set_transmission(Transmission("Автоматической, 8-ступенчатой"))

    def build_body(self):
        self.car.set_body(Body("Внедорожник"))


class SportsCarBuilder(CarBuilder):
    def build_engine(self):
        self.car.set_engine(Engine("3.8 AMT, 610  л. с."))

    def build_transmission(self):
        self.car.set_transmission(Transmission("Роботизированной, 7-ступенчатой"))

    def build_body(self):
        self.car.set_body(Body("Купе"))


# Директор — управляет процессом построения
class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.reset()
        self.builder.build_engine()
        self.builder.build_transmission()
        self.builder.build_body()
        return self.builder.get_car()

sedan_builder = SedanBuilder()
director = CarDirector(sedan_builder)
sedan = director.construct_car()
print("Создан седан:", sedan)

suv_builder = SUVBuilder()
director = CarDirector(suv_builder)
suv = director.construct_car()
print("Создан внедорожник:", suv)

sports_car_builder = SportsCarBuilder()
director = CarDirector(sports_car_builder)
sports_car = director.construct_car()
print("Создан спорткар:", sports_car)