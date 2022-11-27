#Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма
#(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение. Если фирма отработала с прибылью,
#вычислите рентабельность выручки (соотношение прибыли к выручке).
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы
#в расчете на одного сотрудника.

user_proceeds = int(input("Введите значение выручки: "))
user_costs = int(input("Введите значение издержек: "))

if user_proceeds < user_costs:
    print("Фирма работает в убыток")
elif user_proceeds > user_costs:
    print("Фирма работает на прибыль")
    user_profit = user_proceeds - user_costs
    user_rentability = round((user_profit / user_proceeds), 3)
    print(f"Рентабельность выручки фирмы составляет {user_rentability} %")

    user_employes_amount = int(input("Введите количество сотрудников: "))
    profit_per_emplyee = round((user_profit / user_employes_amount), 3)
    print(f"Прибыль на одного сотрудника составила {profit_per_emplyee}")
else:
    print("Фирма 'работает в ноль'")