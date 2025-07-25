def sum_of_even_numbers(*numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return sum(even_numbers)



def vowels_count(string):
    vowels = "aeiouyAEIOUY"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def middle (*numbers):
    total = sum(numbers)
    return total / len(numbers)


