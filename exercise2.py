time_in_sec = input("Введите время в секундах: ")
time_in_mins = round((int(time_in_sec) / 60), 3)
time_in_hours = round((time_in_mins / 60), 3)
results = f"{time_in_hours}:{time_in_mins}:{time_in_sec}"
print(results)