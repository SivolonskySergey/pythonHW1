# Пользователь вводит целое положительное число. Найдите самую большую цифру
# в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = input("Введите целое положительное число: ")
a = int(user_number)
max_value = a % 10

while a > 10:
    a = a // 10
    temp_is_max = a % 10
    if max_value < temp_is_max:
        max_value = temp_is_max
print(f"Самой большой цифрой в числе '{user_number}' является {max_value}")