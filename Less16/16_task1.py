# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег


class kassa(object):
    cash = 0
    def __init__(self, cash):
        self.cash = cash
    def top_up(self, X):
        self.cash += X
    def count_1000(self):
        ost = self.cash // 1000
        print(f'Остаток, тысяч: {ost}')
    def take_away(self, X):
        if (self.cash - X) >= 0:
            self.cash -= X
        else:
            print('Ошибка: в кассе недостаточно денег!')

#пример работы
shop_kassa = kassa(0)
#положить деньги
summa = 2750
shop_kassa.top_up(summa)
print(f'Текущий остаток: {shop_kassa.cash}')
#вывести кол-во тысяч
shop_kassa.count_1000()
#попытка забрать больше, чем в кассе
summa = 5000
shop_kassa.take_away(summa)
#попытка забрать адекватную сумму
summa = 2000
shop_kassa.take_away(summa)
print(f'Текущий остаток: {shop_kassa.cash}')






