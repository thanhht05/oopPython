class test:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
teo = test("Thanh", 19)
print(teo)
        