class Subject:
    def __init__(self, id="", name="", numCredits=0):
        self.id = id
        self.name = name
        self.numCredits = numCredits

    def showSubject(self):
        print("id: ", self.id)
        print("name: ", self.name)
        print("NumCredits: ", self.numCredits)
    def getId(self):
        return self.id

    def handleInput(self):
        self.id = input("Enter subject id: ")
        self.name = input("Enter subject name: ")
        self.numCredits = input("Enter number of credits: ")
    def __str__(self):
        return f"{self.id}, {self.name}, {self.numCredits}\n"

class SubjectManager:
    def __init__(self):
        self.listSubject = []
    def addSubject(self):
        print("Add a new subject ")
        newSubject = Subject()
        newSubject.handleInput()
        self.listSubject.append(newSubject)
    def removeById(self, id):
        found=False
        for subject in self.listSubject:
            if subject.getId() ==id:
                self.listSubject.remove(subject)
                found=True
                print(f"Subject with id '{id}' has been remove.")
                break
        if not found:
            print(f"Subject with '{id}' not found")

    def getData(self):
        n = int(input("Enter quantity subject: "))
        for i in range(n):
            subjectItem = Subject()
            subjectItem.handleInput()
            self.listSubject.append(subjectItem)

    def showAll(self):
        if len(self.listSubject)==0:
            print("Empty")
        else:
            print("\nInformation of all subjects: ")
            for subject in self.listSubject:
                subject.showSubject()
    def sortById(self):
        self.listSubject.sort(key=lambda subject: subject.getId())

    def WriterFile(self):
        with open ("subject.txt", "a") as f:
            for subject in self.listSubject:
                f.write(str(subject))
    def readFile(self):
        with open ("subject.txt", "r") as f:
            for line in f:
                data=line.strip().split(", ")
                id,name,numCredits=data
                print(f"id: {id}, name: {name}, numCredits: {numCredits}")
        
def main():

    manager = SubjectManager()  
    while(True):
        print("Enter 1: To add new subject ")
        print("Enter 2: To add add subject into list ")
        print("Enter 3: To show all information subject ")
        print("Enter 4: To remove subject by id ")
        print("Enter 5: To sort subject by id ")
        print("Enter 6: To writer subject into file ")
        print("Enter 7: To read file ")
        print("Enter 0: To exit ")


        c = int(input("Please enter your selection "))
        if c==0:
            break
        elif c==1:
            manager.addSubject()
        elif c==2:
            manager.getData()
        elif c==3:
            manager.showAll()
        elif c==4:
            id = input("Enter id to remove ")
            manager.removeById(id)
        elif c==5:
            manager.sortById()
        elif c==6:
            manager.WriterFile()
        elif c==7:
            manager.readFile()
        
        


main()
