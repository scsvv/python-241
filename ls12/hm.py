class Form:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student): 
        self.students.append(student)

    def show_all_students(self):
        print(self.title)
        for student in self.students:
            print(student)

class Student:

    def __init__(self, name, surname, age, form : Form):
        self.name = name
        self.surname = surname
        self.age = age
        self.form = form
        form.add_student(self)
        self.subject = dict()
    
    def __str__(self):
        return f'{self.name} | {self.surname} | {self.age}'

    def set_mark(self, name, marks):
        if name in list(self.subject.keys()):
            self.subject[name].append(marks)
            return
        self.subject[name] = [marks]
    

form = Form('7B')
s1 = Student('S1', 'S1', 16, form)
s2 = Student('S2', 'S2', 16, form)
s3 = Student('S3', 'S3', 16, form)

s1.set_mark('Math', 12)
s1.set_mark('Math', 10)
s1.set_mark('Math', 9)
s1.set_mark('Math', 8)


print(s1.subject)
form.show_all_students()

