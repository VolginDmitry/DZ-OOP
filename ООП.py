class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.course_grades:
                lecturer.course_grades[course].append(grade)
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for course in self.grades:
            total_grades += sum(self.grades[course])
            total_courses += len(self.grades[course])
        return round(total_grades / total_courses, 1) 

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade():.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress) or 'нет'}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses) or 'нет'}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for course in self.course_grades:
            total_grades += sum(self.course_grades[course])
            total_courses += len(self.course_grades[course])
        return round(total_grades / total_courses, 1) 

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade():.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")

def average_student_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    return round(total_grades / total_students, 1) 

def average_lecturer_grade(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.course_grades:


            total_grades += sum(lecturer.course_grades[course])
            total_lecturers += len(lecturer.course_grades[course])
    return round(total_grades / total_lecturers, 1) 


# Создаем экземпляры классов
reviewer1 = Reviewer('Семен', 'Проверкин')
reviewer2 = Reviewer('Алиса', 'Проверялкина')

lecturer1 = Lecturer('Андрей', 'Рассказов')
lecturer2 = Lecturer('Агент', 'Смит')

# Созданем студентов
student1 = Student('Иван', 'Иванов', 'мужской')
student2 = Student('Мария', 'Петрова', 'женский')
student3 = Student('Алексей', 'Сидоров', 'мужской')
student4 = Student('Ольга', 'Бузова', 'женский')

# Добавляем курсы для ревьюеров и лекторов
reviewer1.courses_attached.append('Python')
reviewer2.courses_attached.append('Git')

lecturer1.courses_attached.append('Python')
lecturer2.courses_attached.append('Git')

# Добавляем студентов на курсы
student1.courses_in_progress.extend(['Python', 'Git'])
student2.courses_in_progress.extend(['Python', 'Git'])
student3.courses_in_progress.extend(['Python', 'Git'])
student4.courses_in_progress.extend(['Python', 'Git'])

# Проставляем оценки студентам от ревьюеров
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student3, 'Git', 10)
reviewer2.rate_hw(student4, 'Git', 7)

# Студенты выставляют оценки лекторам
student1.rate_lect(lecturer1, 'Python', 9)
student2.rate_lect(lecturer2, 'Git', 8)
student3.rate_lect(lecturer1, 'Python', 10)
student4.rate_lect(lecturer2, 'Git', 9)

# Выводим данные по студентам, лекторам, ревьюерам
print(student1)
print(student2)
print(student3)
print(student4)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)

# средняя оценка студентов за домашние задания по курсу 'Python'
print(f"\nСредняя оценка студентов за домашние задания по курсу 'Python': {average_student_grade([student1, student2, student3, student4], 'Python'):.1f}")

# средняя оценка лекторов за лекции по курсу 'Python'
print(f"Средняя оценка лекторов за лекции по курсу 'Python': {average_lecturer_grade([lecturer1, lecturer2], 'Python'):.1f}")

# средняя оценка студентов за домашние задания по курсу 'Git'
print(f"Средняя оценка студентов за домашние задания по курсу 'Git': {average_student_grade([student1, student2, student3, student4], 'Git'):.1f}")

# средняя оценка лекторов за лекции по курсу 'Git'
print(f"Средняя оценка лекторов за лекции по курсу 'Git': {average_lecturer_grade([lecturer1, lecturer2], 'Git'):.1f}")