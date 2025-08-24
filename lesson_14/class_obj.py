#Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:

    diploma = "economy"


    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.age = age
        self.surname = surname
        self.average_score = average_score

    def change_grade(self, new_grade):
        self.average_score = new_grade

        print(f" Средний бал {self.name} {self.surname} изменено на: {first_student.average_score}")

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Возраст: {self.age}")
        print(f"Средний бал: {self.average_score}")


first_student = Student("Sam", "Winchester", 23, 80 )
first_student.show_info()

print("-"* 80)

first_student.change_grade(99)

first_student.show_info()


