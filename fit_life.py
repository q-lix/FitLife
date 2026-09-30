# Проект FitLife - MVP версия 1.0

# 1. Знакомство
# Узнаем имя пользователя и делаем первую букву заглавной
user_name = input("Введите Ваше имя: ").title()

# Узнаем возраст пользователя и проверяем, что записанно число
flag = True
while (flag):
    user_age = input("Введите Ваш возраст (например: 19): ")
    try:
        user_age = int(float(user_age))
        flag = False
    except ValueError:
        print("Ошибка! Введено не число")


# 2. Сбор данных
# Узнаем вес пользователя в кг
flag = True
while (flag):
    user_weight = input("Введите Ваш вес(например: 67.25): ")
    try:
        user_weight = round(float(user_weight), 2)
        flag = False
    except ValueError:
        print("Ошибка! Введено не число")

# Узнаем вес пользователя в кг
flag = True
while (flag):
    user_height = input("Введите Ваш рост (например: 1.75): ")
    try:
        user_height = round(float(user_height), 2)
        flag = False
    except ValueError:
        print("Ошибка! Введено не число")

# 3. Расчитываем индекс массы тела
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round((user_weight / (user_height ** 2)), 1)

# Подсчет воды: вес * 30 мл
WATER_PER_KG = 30
water_needed = user_weight * WATER_PER_KG / 1000

# 4. Вывод красивого результата
print("=" * 50)  # Рамка для выделения вывода
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_needed:.1f} л. в день")
print()  # Пропуск строки в выводе для красоты
print("Расчет окончен. Будьте здоровы!")
