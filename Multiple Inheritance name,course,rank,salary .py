class Person():
    firstname = None
    lastname = None

    def __init__(self, firstname, lastname):
        self.lastname = lastname
        self.firstname = firstname

    def print_name(self):
        print("Person\'s" + " " + "name is " + " " + self.firstname + " " + self.lastname)

class Student(Person):
    course = None

    def __init__(self, course, firstname, lastname):
        self.course = course
        Person.__init__(self, firstname, lastname)

    def print_course(self):
        print(self.firstname + '\'s'+ " " + "course is {}".format(self.course))

class Faculty(Person):
    rank = None

    def __init__(self, rank, firstname, lastname):
        self.rank = rank
        Person.__init__(self, firstname, lastname)

    def print_rank(self):
        print(self.firstname + '\'s'+ " " + "rank is no.{}".format(self.rank))

class Teaching_Assistant(Student, Faculty):
    salary = None

    def __init__(self, salary, course, rank, firstname, lastname):
        self.salary = salary
        Student.__init__(self, course, firstname, lastname)
        Faculty.__init__(self, rank, firstname, lastname)

    def print_salary(self):
        print(self.firstname + '\'s' +  " " + "salary is {}".format(self.salary))

if __name__ == "__main__":

    Person = Teaching_Assistant(salary = 500000000 , course = "Bachelor Of Science in Electronics Engineering", rank = 1,  firstname = "Jeph", lastname = "Daligdig")
    Person.print_name()
    Person.print_course()
    Person.print_rank()
    Person.print_salary()

