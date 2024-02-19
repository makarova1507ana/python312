from tamagochi import Tamagochi
from timeGame import Time
import time
import re
import math

class UserInterface():
    def __init__(self):
        self.userinterface()
    def userinterface(self):
        def line():
            print("------------------------------------------")
        while True:
            print("\nฅ^•ﻌ•^ฅ MEOW Поиграем в тамагочи?  MEOW ฅ^•ﻌ•^ฅ")
            command_start = input("""
1.Начать игру
2.Выйти из игры 
""")
            if command_start == "1":
                name = input("введите имя питомца: ")
                pattern = r'^[А-яЁёA-z\s]+$'
                if re.match(pattern,name) == None or name.isspace():
                    print("Назови питомца нормально")
                else:
                    pet = Tamagochi(name)
                    create_time = time.time()#костыль1
                    my_time = Time()
                    my_time.start()
                    my_time.start_time
                    while True:
                        my_time.update_attribute(pet)
                        my_time.attribute_reduction(pet)
                        pet.the_death()
                        command_base = input("""
1. Показать характеристики Питомца
2. Поесть
3. Поспать
4. Поиграть
5. Ничего не делать
6. Выйти из игры
""")
                        if command_base == "1":
                            line()
                            pet.random_event_satiety()
                            pet.random_event_sleep()
                            pet.random_event_happy()
                            print(pet)
                            pet.the_death()
                            now_time = time.time()#костыль 2
                            last_time = now_time - create_time #костыль 3
                            print(f"Ваш питомец живёт уже:{round(last_time)} секунд")
                        elif command_base == "2":
                            pet.add_food()
                            pet.random_event_satiety()
                            pet.random_event_sleep()
                            pet.random_event_happy()
                            print(pet)
                            pet.the_death()
                        elif command_base == "3":
                            print("""
∩――――∩
||  ∧ ﾍ||
||(* ´ ｰ`) ZZzz
|ﾉ^⌒⌒づ`￣  ＼
(　ノ　　⌒ ヽ ＼
＼　　||￣￣￣￣￣||
 ＼,ﾉ||
""")
                            pet.add_sleep()
                            pet.random_event_satiety()
                            pet.random_event_sleep()
                            pet.random_event_happy()
                            print(pet)
                            pet.the_death()
                        elif command_base == "4":
                            line()
                            pet.game_played()
                            pet.random_event_satiety()
                            pet.random_event_sleep()
                            pet.random_event_happy()
                            print(pet)
                            pet.the_death()
                        elif command_base == "5":
                            line()
                            pet.nothing()
                            pet.random_event_satiety()
                            pet.random_event_sleep()
                            pet.random_event_happy()
                            print(pet)
                            pet.the_death()
                        elif command_base == "6":
                            line()
                            pet.happy = 0
                            pet.sleep = 0
                            pet.satiety = 0
                            pet.the_death()
                            break
                        else:
                            print("Ошибка")
                            pet.random_event_satiety()
                            pet.random_event_sleep()
                            pet.random_event_happy()
                            pet.the_death()
            elif command_start == "2":
                break
            else:
                print("Ошибка")
user = UserInterface()


