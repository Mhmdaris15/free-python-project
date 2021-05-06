""" # Templating
class Customer: # --> Template
    pass

# Instansiate
customer1 = Customer() # --> Object / Instance
customer2 = Customer()
customer3 = Customer()

customer1.name = 'Muhammad Aris'
customer1.saldo = 70000000

customer2.name = 'Adam Darusman'
customer2.saldo = 50000000

customer3.name = 'Mila Nabila'
customer3.saldo = 40000000

print(Customer.__dict__)
print(customer1.__dict__)
print(customer2.__dict__) """



""" class Student:
        # __init__ akan dieksekusi langsung pada saat objek pertama kali dibuat
    def __init__(self, Name, Major, Gender):
        self.name = Name
        self.major = Major
        self.gender = Gender

student1 = Student('Aris', 'Informatics and Computer science', 'Male')
student2 = Student('Adam', 'Robotics', 'Male')
student3 = Student('Mila', 'Network Engineer', 'Female')

print(student1.name, student1.major, student1.gender)
print(student2.gender)
print(student3.major) """



""" class Student:
    # Class Variable
    Sum = 0
    def __init__(self, Name, Major, Gender):
        # Instance Variable
        self.name = Name
        self.major = Major
        self.gender = Gender
        
        Student.Sum += 2 #Cara Memanggil Class Variabel (Class + VariableName)

student1 = Student('Aris', 'Informatics and Computer science', 'Male')
print(Student.Sum)
student2 = Student('Adam', 'Robotics', 'Male')
print(Student.Sum)
student3 = Student('Mila', 'Network Engineer', 'Female')
print(Student.Sum)
print(Student.__dict__) """