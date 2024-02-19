from tamagochi import Tamagochi
import time
import math
#
# class Pet: #Отладочный класс
#     def __init__(self, name, sleep, happy, satiety):
#         self.name = name
#         self.sleep = sleep
#         self.happy = happy
#         self.satiety = satiety
#
#     def __str__(self): #метод отладочной печати
#         return (f'''
#         ------------------------
#         Name: {self.name}
#         Sleep: {self.sleep}
#         Happy: {self.happy}
#         Satiety: {self.satiety}
#         ------------------------
#         ''')

class Time:# инициализация
    def __init__(self):
        self.start_time = None

    def start(self):  # renamed from start_time to start
        self.start_time = time.time()

    def early_time(self): # метод старта и отслеживания времени
        if self.start_time is None:
            return 0
        else:
            return time.time() - self.start_time

    def update_attribute(self, pet): #метод обновления атрибутов
        early_time = self.early_time()
        if early_time >= 2 * 60:
            num_decrements = int(early_time // (2 * 60))
            pet.sleep -= num_decrements
            pet.happy -= num_decrements
            pet.satiety -= num_decrements
            self.start_time += num_decrements * 2 * 60

    def attribute_reduction(self, pet): #метод уменьшения атрибутов
        pet.sleep -= 1
        pet.happy -= 1
        pet.satiety -= 1

    def __str__(self):
        str_start_time = str(self.start_time)
        return str_start_time
#
# my_pet = Tamagochi("Kokoshka")
# my_time = Time()
# my_time.start()
#
#
# while True:
#     my_time.update_attribute(my_pet)
#     my_time.attribute_reduction(my_pet)
#     print(my_pet)
#     time.sleep(3)

# сделать объект в классе пет
# следить за этим объектом в классе time
# сделать нормальный вывод данных
# и до работать код
