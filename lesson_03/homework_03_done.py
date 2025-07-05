alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_sea_area = black_sea_area + azov_sea_area
print("Площа чорного моря та Азовського моря разом становлять:", total_sea_area, "км2" )

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_items = 375291
items_first_second = 250449
items_second_third = 222950

y = items_first_second + items_second_third - total_items
x = items_first_second - y
z = items_second_third - y

print("На першому складі", x, "товарів.")
print("На другому складі", y, "товарів.")
print("На третьому складі", z, "товарів.")



# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

payment_per_month = 1179
time = 1.5 * 12
final_cost = payment_per_month * time
print("Кінцева вартість пк", final_cost, "грн")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("Остача від ділення:")
print("a) 8019 : 8 =", 8019 % 8)
print("b) 9907 : 9 =", 9907 % 9)
print("c) 2789 : 5 =", 2789 % 5)
print("d) 7248 : 6 =", 7248 % 6)
print("e) 7128 : 5 =", 7128 % 5)
print("f) 19224 : 9 =", 19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_large = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total_cost = pizza_large + pizza_medium + juice + cake + water
print("Іринці знадобиться:", total_cost, "грн")




# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
picture_amount = 232
pages_amount_required = picture_amount // 8
print("Ігорю щоб розмістити всі фото знадобиться:", pages_amount_required, "сторінок")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_usage_per_100km = 9
tank_capacity = 48
total_fuel_usage = ( distance // 100) * fuel_usage_per_100km
refills_needed = total_fuel_usage // tank_capacity
print("Для такої подорожі їм знадобиться",total_fuel_usage,"літрів бензину")
print("Щонайменше поповнювати бак їм потрибно буде",refills_needed,"разів")

