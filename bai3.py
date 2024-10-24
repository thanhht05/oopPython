class Employee:
    EmployeeCount=0
    def __init__(self,id,fullName,birthDay,phoneNumber,email):
        self.id=id
        self.fullName=fullName
        self.birthDay=birthDay
        self.phoneNumber=phoneNumber
        self.email=email
        self.EmployeeCount+=1
    def __str__(self):
        return f"ID: {self.id}, FullName: {self.fullName}, BirthDay: {self.birthDay}, Phone: {self.phoneNumber}, Email: {self.email}"

class Fresher(Employee):
    def __init__(self, id, fullName, birthDay, phoneNumber, email,graduationDate, education):
        super().__init__(id, fullName, birthDay, phoneNumber, email)
        self.graduationDate=graduationDate
        self.education=education
    def __str__(self):
        return super().__str__() + f"graduationDate: {self.graduationDate}, Education: {self.education}"
a = Fresher(1,"thanh","12/12/2002", "0923293","thanh.com","good","husc")
print(a)


        
        