import random
class Tamagochi:#инициализация класса
    def __init__(self, name):
        self.name = name
        self.happy = 100
        self.satiety = 100
        self.sleep = 100

    def __str__(self):#метод перегрузки для печати
        return (f'''
------------------------
Name: {self.name}
Sleep: {self.sleep}
Happy: {self.happy}
Satiety: {self.satiety}
-----------------------''')

    def random_event_satiety(self): #метод случайного события
        event = random.choice(range(1,8))
        if event == 1:
            self.satiety -=20
            print(f"У {self.name} заболел живот ")
        elif event == 8:
            self.satiety +=10
            print(f"Питомец {self.name} нашёл редкий корм!")
    def random_event_sleep(self):#метод стучайного события
        event = random.choice(range(1,8))
        if event == 1:
            self.sleep -=20
            print(f"Питомец {self.name} сильно испугался")
        elif event == 8:
            self.sleep +=10
            print(f"Питомец {self.name} активен как никогда!")
    def random_event_happy(self):#метод стучайного события
        event = random.choice(range(1,8))
        if event == 1:
            self.happy -=20
            print(f"""
У питомца {self.name} апатия
             ／＞　 フ
            | 　_　_| 
          ／` ミ＿xノ 
         /　　　　 |
        /　 ヽ　　 ﾉ
        │　　|　|　|
    ／￣|　　 |　|　|
   | (￣ヽ＿_ヽ_)__)
   ＼二)
""")
        elif event == 8:
            self.happy +=10
            print(f"Питомец {self.name} счастлив!")
    def add_food(self ):#метод еды
        self.satiety += 20
        if self.satiety >100:
            self.satiety -=40
            print(f"Твоему {self.name} очень плохо от переедания")
    
    def add_sleep(self):#метод сна
        self.sleep += 20
        if self.sleep >100:
            self.sleep -=40
            print(f"{self.name} плохо спал, чувствует себя ужасно")

    def the_death(self):#метод смерти
        if self.satiety <= 0 or self.sleep <= 0 or self.happy <= 0 :
            print('ฅ^xﻌx^ฅ НАСТУПИЛА СМЭРТЬ ฅ^xﻌx^ฅ')
            del Tamagochi

    def game_played(self):#метод игры
        self.happy += 20
        self.satiety -= 20
        self.sleep -= 20
        if self.happy > 100:
            print(f"Не заставляй {self.name} играть")
            self.happy -=40
    
    def nothing(self):#метод ничегонеделанья
        self.happy -= 20
        self.satiety -= 20
        self.sleep -= 20
        





