# PROYEK PERUSAHAAN (SISTEM MANAJEMEN SUMBER DAYA MANUSIA)

# GAJI SETIAP KARYAWAN DAN PROFESINYA

# PENGELUARAN PERUSAHAAN UNTUK GAJI PARA PEGAWAI

# MENGGUNAKAN PARADIGMA BAHASA PEMROGRAMAN OBJECT ORIENTED PROGRAMMING (PYTHON OOP)


class Employee:
    overtime_fee = 100
    def __init__(self, name, age, income, additional_incentive):
        self.name = name 
        self.age = age
        self.income = income
        self.add_income = 0
        self.add_incent = additional_incentive
    def overtime(self):
        self.add_income += self.add_incent
    def new_project(self, amount_project):
        self.add_income += amount_project
    def total_salary(self):
        return self.income + self.add_income

""" Di perusahaan ini, seorang analis data yang masuk umumnya berusia 21, 
memiliki pendapatan senilai 6.500.000 dan insentif lembur senilai 100.000. 
Kemudian, untuk seorang ilmuwan data yang masuk umumnya berusia 25, 
memiliki pendapatan senilai 12.000.000, dan insentif lembur senilai 150.000. 
Di sisi lain, untuk tenaga lepas, hanya terdapat pendapatan umum senilai 4000000 
untuk pembersih data dan 2500000 untuk dokumenter teknis.  

Freelance akan dapat 5% dari pendapatan proyek
Data Scientist dapat 10% dari pendapatan proyek
"""
class Freelance(Employee):
    def __init__(self, name, age, income):
        super().__init__(name, age, income, 0)
    def new_project(self, amount_project):
        self.add_income += amount_project * 0.05

class DataAnalys(Employee):
    def __init__(self, name, age=21, income=1500, additional_incentive=270):
        super().__init__(name, age, income, additional_incentive)

class DataScientist(Employee):
    def __init__(self, name, age=25, income=3400, additional_incentive=320):
        super().__init__(name, age, income, additional_incentive)
    def new_project(self, amount_project):
        self.add_income += amount_project * 0.1

class DataCleaner(Freelance):
    def __init__(self, name, age, income=1200):
        super().__init__(name, age, income)

class TechnicalDocumenter(Freelance):
    def __init__(self, name, age, income=850):
        super().__init__(name, age, income)

# COMPANY STUFF
class Company:
    def __init__(self, name, address, telephoneNumber):
        self.name = name
        self.address = address
        self.telephoneNumber = telephoneNumber
        self.Employee_List = []
    def activate_employees(self, employee_name):
        self.Employee_List.append(employee_name)
    def unactivate_employees(self, employee_name):
        inactive_employee = None
        for i in self.Employee_List:
            if i.name == employee_name:
                inactive_employee = i
                break
        if inactive_employee is not None:
            self.Employee_List.remove(inactive_employee)
    def total_outcome(self):
        outcome = 0
        for i in self.Employee_List:
            outcome += i.total_salary()
        return outcome
    def search_Emplyees(self, employee_name):
        for i in self.Employee_List:
            if i.name == employee_name:
                return i
        return None
                

# Create object karyawan sesuai dengan tugasnya masing-masing
John = DataAnalys(name='John Dalton', age=27)                   # Data Analyst, 27 y.o, 
Marie = DataScientist(name='Marie Curry', age=19, income=4000)  # Data Scientist, 19 y.o, USD 4000
Nikita = DataAnalys(name='Nikita Sulkyovo', income=1750)        # Data Analyst, USD 1750
Joseph = TechnicalDocumenter(name='Joseph Stalin', age=22)      # Technical Documenter, 22 y.o
Sukhov = DataCleaner(name='Sukhov Gorbanichev', age=22)         # Data Cleaner, 22 y.o