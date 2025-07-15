# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    multiplier = 1
    while multiplier <= 25 / number:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)



# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two (a, b):
    return a + b
print(sum_of_two(5, 5))



# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def middle (*numbers):
    total = sum(numbers)
    return total / len(numbers)
print(middle(5, 5, 5))



# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string):
    return string[::-1]
print(reverse_string("Hello"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word (*words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(longest_word("Bird", "Cat", "Pacific", "Castle"))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    return index if index != -1 else -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1



# # task 7
def sum_of_even_numbers(*numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return sum(even_numbers)
print(sum_of_even_numbers(6, 6))

# # task 8
def vowels_count(string):
    vowels = "aeiouyAEIOUY"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
print(vowels_count(str1))

# # task 9
def same_elements(list1, list2):
    return list(set(list1) & set(list2))
result = same_elements([2,4,5,6,9,10], [4,6,8,10,11])
print(result)

# # task 10
def count_words(text):
    words = text.split()
    return len(words)
print(count_words(str1))
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""