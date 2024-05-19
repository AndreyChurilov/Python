# Создайте класс Autobus, который наследуется от класса Transport.
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.

class Transport:
   def __init__(self, name, max_speed, mileage):
      self.name = name
      self.max_speed = max_speed
      self.mileage = mileage

   def seating_capacity(self, capacity):
      return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

class Autobus(Transport):
   def seating_capacity(self, capacity = 50):
      return super().seating_capacity(capacity)
   
RenoCar = Autobus('Renaul Logan', 180, 12)
print(RenoCar.seating_capacity())

