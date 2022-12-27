# Create a class named ‘Employee’ having the following members: id and name
# Another class named ‘HourlyEmployee’ should have the data members ‘hours_worked’ and ‘hour_rate’ .
# Another class named ‘CalculatePayroll’ inherits both the ‘Employee’ and ‘HourlyEmployee’ classes and
# should have a method which will print the payroll of employee along with the name and id.
# Formula to calculate payroll is-> number of hours worked * hour rate

class employee:
    def __init__(self):
        self.id=int(input("Enter id :  "))
        self.name=input("Enter name : ")
class hourlyemp(employee):
    def __init__(self,):
        super().__init__()
        self.hours=int(input("Hours worked : "))
        self.hourrate=int(input("hour rate : "))


class payroll(hourlyemp):
    def __init__(self):
        hourlyemp.__init__(self)
        self.salary=""
    def monthsalary(self):
        return self.hours*self.hourrate
    def printdet(self):
        self.salary=self.monthsalary()
        print("emp-id \t emp_name \t hours_worked \t hour_rate \t salary ")
        print(f"{self.id} \t {self.name} \t\t {self.hours} \t\t\t {self.hourrate} \t\t {self.salary}")
        
num=int(input("Enter the number of employees"))
emp=[]
for i in range(num):
    obj=payroll()
    emp.append(obj)

print("\n\n\n monthly salaries of employees")
for i in emp:
    i.printdet()
