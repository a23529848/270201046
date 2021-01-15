 # It is not efficient ass well as examples but I tried

class Employee:
  def __init__(self):
      self.name = " "
      self.salary = " "

  def __str__(self):
      return "Name:" + self.get_name() + "\nSalary:" + str(self.get_salary())

  def set_salary(self, salary):
      self.salary = salary

  def get_salary(self):
      return self.salary

  def set_name(self, name):
      self.name = name

  def get_name(self):
      return self.name


class Company:
  def __init__(self):
      self.employeeList = []

  def set_employeeList(self, employeeList):
      self.employeeList = employeeList

  def get_employeeList(self):
      return self.employeeList

  def addEmployee(self, new_employee, salary):
      if new_employee not in self.employeeList:
          self.employeeList.append((new_employee, salary))
      else:
          print("You had already appended the employee in your list")

  def averageSalary(self):
      summation = 0
      for employee in self.employeeList:
          summation += int(employee[1])
      average = summation / len(self.employeeList)
      return average

  def showInfo(self):
      for i in self.employeeList:
          print(i)


company = Company()
# Employee1
e1 = Employee()
e1.set_name("Berke")
e1.set_salary("2500")
# Employee2
e2 = Employee()
e2.set_name("Ahmet")
e2.set_salary("3000")
# Employee3
e3 = Employee()
e3.set_name("İsmet")
e3.set_salary("1500")

company.addEmployee(e1.get_name(), e1.get_salary())
company.addEmployee(e2.get_name(), e2.get_salary())
company.addEmployee(e3.get_name(), e3.get_salary())

print(company.get_employeeList())
print(company.averageSalary())
