class Employee:
  def __init__(self, name, age, salary, employment_years, get_annual_salary):
    self.name = name
    self.age = age
    self.salary = salary
    self.employment_years = employment_years
    self.get_annual_salary = get_annual_salary
    return self.salary * 12

  def __str__(self):
      return f"my name is: {self.name}, my age is: {self.age}years old, my salary is: {self.salary}, working years: {self.employment_years}, and salary is: {self.get_annual_salary}"
  
class Manager(Employee):
    def manger(self, name, age, salary, employment_years, bonus_percentage, get_bonus):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = employment_years
        self.bonus_percentage = bonus_percentage
        self.get_bonus = get_bonus
        return self.bonus_percentage * salary

    def __str__(self):
        return f"my name is: {self.name}, my age is: {self.age}years old, my salary is: {self.salary}, working years: {self.employment_years}, and bonus is: {self.get_bonus}"

employee = ["name", "age", "salary", "years", "annual_salary"]
manager = ["name", "age", "salary", "years", "bonus_percentage", "bonus"]



        
def main():
    print("Welcome to the HR Pro")
    print("option:" )
    print(Employee)
    for p1 in employee:
        print(input(employee))
    print(Manager)
    for p2 in manager:
        print(input(manager))
    return main
if __name__ == '__main__.Employee':

    main()
