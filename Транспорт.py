# речной - паромы, баржи, речные трамваи, суда на воздушных подушках; морской - круизные лайнеры,
# тяжеловозы, танкеры, контейнеровозы

# Транспортное средство
class Vehicle:
    pass


# Водный транспорт
class WaterTransport(Vehicle):
    pass


# Речной транспорт
class RiverTransport(WaterTransport):
    pass


# Баржа
class Barge(RiverTransport):
    pass


# Паром
class Ferry(RiverTransport):
    pass


# Морской транспорт
class SeaTransport(WaterTransport):
    pass


# Танкер
class Tanker(SeaTransport):
    pass


# Прямоугольник
class AirTransport(Vehicle):
    pass


# Авиация
class Aviation(AirTransport):
    pass


# Самолет
class Airplane(Aviation):
    pass


# Воздухоплавание
class Aeronautics(AirTransport):
    pass


# Дирижабль
class Airship(Aeronautics):
    pass


# Наземный транспорт
class GroundTransport(Vehicle):
    pass


# Железнодорожный транспорт
class RailwayTransport(GroundTransport):
    pass


# Электричка
class ElectricTrain(RailwayTransport):
    pass


# Автомобильный транспорт
class AutomobileTransport(GroundTransport):
    pass


# Машина
class Car(AutomobileTransport):
    pass


# Велосипедный транспорт
class BicycleTransport(GroundTransport):
    pass


# Велосипед
class Bike(BicycleTransport):
    pass


# Транспорт, управляемый животными
class TransportDrivenByAnimals(GroundTransport):
    pass


# Собачья упряжка
class DogTeam(TransportDrivenByAnimals):
    pass


# Космический транспорт
class SpaceTransport(Vehicle):
    pass


# Ракета
class Rocket(SpaceTransport):
    pass
