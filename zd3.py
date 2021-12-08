#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В магазине Сладкая долина сегодня распродажа, на каждый товар стоимостью от 100 рублей скидка 50%,
# а на батончики Twix скидка 25%.
# Напишите программу, которая подсчитает итоговый чек.
def magaz(kassir, **candies):
    print("Магазин конфет Сладкая долина")
    print(f"Кассир: {kassir}")
    summ = 0
    for candies, cost in candies.items():
        summ += cost
        if candies == "Twix":
            cost = (cost / 100) * 75
        if cost > 100:
            cost /= 2
        print(f"{candies}: {cost}")

    print(f"Итоговая стоимость: {summ}")


if __name__ == "__main__":
    magaz(
        "Швецова Ксения",
        Snikers=79, Mars=59,
        Twix=59, Korkunov=199
    )
