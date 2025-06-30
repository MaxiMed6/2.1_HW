# task 01
print("Hello", end = " ")
print("world!")

# task 02
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03
for letter in "Hello world!":
    print(letter)

# task 04
apples = 2
banana = 4 * apples

# task 05
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2
total_tree = apple_tree + pear_tree + plum_tree


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temp_before_dinner = 5
temp_after_dinner = temp_before_dinner - 10
temp_evening =temp_after_dinner + 4


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys // 2
total_children = boys + girls - 3
# решил без лишних переменных записать



# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) // 2
total_books = first_book + second_book + third_book
print(total_books)