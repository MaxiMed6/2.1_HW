data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
def numbers_sum(number):
    result = 0
    numbers_list = number.split(",")
    for num in numbers_list:
        try:
            number_value = int(num)
            result += number_value
        except ValueError:
            return "Не можу це зробити!"
    return result


for item in data:
    print(numbers_sum(item))