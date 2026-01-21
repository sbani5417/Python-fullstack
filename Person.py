class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_Student(self):
        self.display_info()
        print("Roll No:", self.roll_no)


s1 = Student("Sakshi", 21, 135)
s1.display_Student()
