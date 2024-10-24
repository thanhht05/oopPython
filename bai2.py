class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"

class Worker(Person):
    def __init__(self, name, age, gender, address, level):
        super().__init__(name, age, gender, address)
        self.level = level

    def __str__(self):
        return super().__str__() + f"Level: {self.level}"

class Engineer(Person):
    def __init__(self, name, age, gender, address, trainIndustry):
        super().__init__(name, age, gender, address)
        self.trainIndustry = trainIndustry

    def __str__(self):
        return super().__str__() + f"trainIndustry: {self.trainIndustry}"

class Staff(Person):
    def __init__(self, name, age, gender, address, work):
        super().__init__(name, age, gender, address)
        self.work = work

    def __str__(self):
        return super().__str__() + f"work: {self.work}"

class ManagerPerson:
    def __init__(self):
        self.listPerson = []

    def add_person(self, person):
        self.listPerson.append(person)

    def show_all_persons(self):
        if len(self.listPerson) == 0:
            print("No persons to show.")
        else:
            for person in self.listPerson:
                print(person)

def main():
    manager = ManagerPerson()
    while True:
        print("Enter 1: To add Person ")
        print("Enter 2: To show information of all Persons ")
        a = int(input("Please enter your selection: "))
        if a == 1:
            print("Enter a: To add Engineer ")
            print("Enter b: To add Staff ")
            print("Enter c: To add Worker ")

            c = input("Please choose the type of person (a/b/c): ")
            
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            address = input("Enter address: ")

            if c == 'a':
                trainIndustry = input("Enter train industry: ")
                engineer = Engineer(name, age, gender, address, trainIndustry)
                manager.add_person(engineer)

            elif c == 'b':
                work = input("Enter work: ")
                staff = Staff(name, age, gender, address, work)
                manager.add_person(staff)

            elif c == 'c':
                level = input("Enter level: ")
                worker = Worker(name, age, gender, address, level)
                manager.add_person(worker)

        elif a == 2:
            manager.show_all_persons()

main()
