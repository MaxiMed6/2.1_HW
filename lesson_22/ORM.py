from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
from faker import Faker
import random
import time


DATABASE_URL = "postgresql://postgres:5013@localhost:5432/ORM"
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(bind=engine)

student_course_association = Table(
    "student_course",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    courses = relationship("Course", secondary=student_course_association, back_populates="students")

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.first_name} {self.last_name}', email='{self.email}')>"

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    students = relationship("Student", secondary=student_course_association, back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}')>"


def create_tables():
    print("---Tables are creating---")
    Base.metadata.create_all(engine)
    print("---Tables has created---")

def create_sample_data():
    session = SessionLocal()

    if session.query(Student).first() or session.query(Course).first():
        print("Already full")
        session.close()
        return

    courses_data = [
        ("Вища математика", "Основи математичного аналізу та алгебри"),
        ("Програмування на Python", "Вивчення мови програмування Python"),
        ("Англійська мова", "Академічний рівень англійської мови"),
        ("Фізика", "Загальна фізика для технічних спеціальностей"),
        ("Історія України", "Історія України від давнини до сьогодення")
    ]

    courses = []
    for name, description in courses_data:
        course = Course(name=name, description=description)
        session.add(course)
        courses.append(course)

    session.commit()
    print(f"Created {len(courses)} courses")

    fake = Faker("uk_UA")

    students = []
    for i in range(20):
        first_name = fake.first_name()
        last_name = fake.last_name()


        base_email = f"{first_name.lower()}.{last_name.lower()}"
        email = f"{base_email}{int(time.time() * 1000)}@gmail.com"

        student = Student(first_name=first_name, last_name=last_name, email=email)
        session.add(student)
        students.append(student)

    session.commit()
    print(f"Created {len(students)} students")

    for student in students:
        num_courses = random.randint(1, 3)
        selected_courses = random.sample(courses, num_courses)
        student.courses.extend(selected_courses)

    session.commit()
    print("Students are randomly sent in the courses")
    session.close()

def add_student(first_name, last_name, email, course_ids=None):
    print(f"--- Adding student: {first_name} {last_name} ({email}) ---")
    session = SessionLocal()

    existing_student = session.query(Student).filter_by(email=email).first()
    if existing_student:
        print(f"Student with  {email} already created: {existing_student}")
        session.close()
        return existing_student.id

    new_student = Student(first_name=first_name, last_name=last_name, email=email)
    session.add(new_student)
    session.commit()

    if course_ids:
        courses_to_add = session.query(Course).filter(Course.id.in_(course_ids)).all()
        new_student.courses.extend(courses_to_add)
        session.commit()
        print(f"Student added to : {[c.name for c in courses_to_add]}")
    else:
        print("Student added without courses.")

    student_id = new_student.id
    session.close()
    return student_id

def get_students_by_course(course_id):
    print(f"--- Students in the course with ID: {course_id} ---")
    session = SessionLocal()

    course = session.query(Course).filter_by(id=course_id).first()
    if not course:
        session.close()
        return []

    students = course.students
    for student in students:
        print(f"  - {student.first_name} {student.last_name} ({student.email})")
    print(f"Students total: {len(students)}")
    session.close()
    print("-" * 20)
    return students

def update_student(student_id, first_name=None, last_name=None, email=None):
    print(f"Updating the student with ID {student_id}")
    session = SessionLocal()

    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print(f"Student with ID {student_id} is missing.")
        session.close()
        return None

    if first_name:
        old_name = student.first_name
        student.first_name = first_name
        print('Name has been updated')

    if last_name:
        old_last_name = student.last_name
        student.last_name = last_name
        print("Last_name has been updated")

    if email:
        old_email = student.email
        student.email = email
        print("Email has been updated")

    session.commit()
    print(f"Updated student {student}")
    session.close()
    return student

def delete_student(student_id):
    print(f"Deleting student with ID {student_id}")
    session = SessionLocal()

    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print(f"Student with ID {student_id} is missing.")
        session.close()
        return False

    session.delete(student)
    session.commit()
    print(f"The student {student.first_name} is deleted")
    session.close()
    return True

def drop_all_tables():
    print("--- Видалення всіх таблиць ---")
    Base.metadata.drop_all(engine)
    print("Всі таблиці видалено.")
    print("-" * 20)


if __name__ == "__main__":
    create_tables()
    create_sample_data()

    session = SessionLocal()
    course1 = session.query(Course).first()
    course2 = session.query(Course).offset(1).first()
    session.close()

    new_student1_id = add_student("Іван", "Франко", "ivan.franko@example.com")

    if course1:
        get_students_by_course(course1.id)


    if new_student1_id:
        update_student(new_student1_id, first_name="Дмитро")

    drop_all_tables()
    print("Роботу з базою даних завершено.")
