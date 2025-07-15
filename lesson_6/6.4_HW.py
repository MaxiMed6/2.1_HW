numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_numbers = 0
for num in numbers:
    if num % 2 == 0:
        even_numbers += num
print("Сумма парных чисел:", even_numbers)