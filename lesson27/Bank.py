# —------------------------------- Задача —--------------------------------#
# Реализуйте систему банковских счетов с использованием наследования.
# Создайте базовый-абстрактный класс, а затем подклассы, представляющие "Текущий счет",
# "Сберегательный счет"(деньги снять нельзя, но они увеличиваются на определенный процент каждый год) и
# "Кредитный счет"(можно снять деньги, но будет специальный атрибут долг, который будет расти каждый год на орпеделенный процент).
# Реализуйте методы для внесения и снятия средств.


# Создайте базовый-абстрактный класс Счет
# * метод пополнения
# * метод просмотра
# * метод снятия
#
# класс "Текущий счет"
# * метод пополнения
# * метод просмотра
# * метод снятия

# "Сберегательный счет"(деньги снять можно по истечению конкретного срока, но они увеличиваются на определенный процент каждый год) и
# * метод пополнения
# * метод просмотра
# * метод снятия (подумать над правилами)

# "Кредитный счет"(можно снять деньги, но будет специальный атрибут долг, который будет расти каждый год на орпеделенный процент).
# * метод пополнения
# * метод просмотра
# * метод снятия


from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, balance: float = 0):
        self._balance = balance
    # @property
    # def balance(self):
    #     return self._balance
    #
    # @balance.setter
    # def balance(self, money):
    #     self._is_money(money)
    #     self._balance = money

    def view(self):
        return self._balance
    def add(self, money):
        self._is_money(money)
        self._balance += money
    @staticmethod
    def _is_money(money):
        if not ((type(money) in [float, int]) and money > 0):
            raise "Передаваемая сумма меньше 0 или не int или не float"


    @abstractmethod
    def withdraw(self, money):
        pass


class ActiveAccount(Account):

    def withdraw(self, money):
        self._is_money(money)
        if self._balance < money:
            raise ValueError('не хватает денег на балансе')

        self._balance -= money
        return self._balance


class SavingsAccount(Account):
    def __init__(self, balance: float, years: int): # years - на сколько положили
        super().__init__(balance)
        self.__years = years
        for i in range(years):
            self._balance += self._balance * 13 / 100  # 13 - процентная ставка типа ежегодная

    def withdraw(self, years: int):# years -  сколько прошло
        print("вот столько денег:", self.view())
        if years >= self.__years:
            self._balance = 0
            return 0
        print('Приходите позже, ваше время еще не пришло')



class CreditAccount(Account):
    def __init__(self, balance: float, years: int):  # years - на сколько положили
        super().__init__(-balance)
        self.__years = years
        # for i in range(years):
        #     self._balance -= self._balance * 13   # 13 - процентная ставка типа ежегодная

    def withdraw(self, money: float): # увеличение долга
        self.is_money(money)
        self._balance -= money

    def wait_a_few_days(self, days: int):
        duty = 50000 - self.all_the_money
        if duty <= 0:
            pass
        else:
            for i in range(days):
                duty = 50000 - self.all_the_money
                self.all_the_money -= duty * 5 / 100  # 5 - процентная ставка ежедневная


# user_account = ActiveAccount()
# user_account.add(100)
# print(user_account.view())

# saving_account = SavingsAccount(2)
# saving_account.withdraw(1)
# print(saving_account.view())
credit = CreditAccount(1000, 5)
print(credit.view())
credit.add(1000)
print(credit.view())



