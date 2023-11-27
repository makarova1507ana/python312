# функции для работы с кошельком
# - Снятие нажмите 2
# - Пополнение нажмите 3
is_valid_money = lambda x: x >= 0

def refill(balance, money):
    if is_valid_money(float(money)):
        return balance + float(money)
    return balance

def withdrawal(balance, money):
    if is_valid_money(float(money)) and is_valid_money(balance - float(money)):
        return balance - float(money)
    return balance