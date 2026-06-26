class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if isinstance(student, Person):
            self.students.append(student)
        else:
            raise ValueError("Only instances of Person can be added as students.")

    def list_students(self):
        return [student.greet() for student in self.students]
    
class Undergraduate(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def greet(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and I am majoring in {self.major}."
    
def main():
    uni = University("Tech University")
    
    student1 = Undergraduate("Alice", 20, "Computer Science")
    student2 = Undergraduate("Bob", 22, "Mechanical Engineering")
    
    uni.add_student(student1)
    uni.add_student(student2)
    
    for greeting in uni.list_students():
        print(greeting)

if __name__ == "__main__":
    main()
    