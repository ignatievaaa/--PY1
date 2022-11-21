salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(months):  # выбираем цикл с заданным количеством шагов
   delta = spend - salary  # расходы в текущем месяце
   spend *= 1 + increase  # ежемесячное увеличение расходов
   money_capital += delta  

print(round(money_capital))
