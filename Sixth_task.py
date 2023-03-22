my_cash = int(input("Напишите свою выручку"))
my_lost = int(input("Напишите издержки"))
total_cash = my_cash - my_lost  ## валовая прибыль

profitability = total_cash / my_cash * 100
print(profitability)
employs = int(input("Напишите кол-во сотрудников"))
employer_cash = total_cash / employs  ##персональная прибыль сотрудников
print("Прибыль сотрудника" + employer_cash)
