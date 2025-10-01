from Person import Person
from utils import printNotNumerError, printNotStringError, printShouldBeError

class Employee(Person):
    def __init__(self, id: int, name: str, age: int) -> None:
        super().__init__(id, name, age)
        
        try:
            self._field_of_work = input("Enter Field Of Work: ")
        except KeyboardInterrupt:
            print("\nUser interrupted with Ctrl+C, exiting...")
            raise KeyError()
        if self._field_of_work.isdigit():
            printNotStringError("Field of Work", self._field_of_work)
            raise ValueError()
        
        try:
            salary = input("Enter Salary: ")
        except KeyboardInterrupt:
            print("\nUser interrupted with Ctrl+C, exiting...")
            raise KeyError()
        if not salary.isdigit():
            printNotNumerError("Salary", salary)
            raise ValueError()
        self._salary = float(salary)

    def getFieldOfWork(self) -> str:
        return self._field_of_work
    
    def getSalary(self) -> float:
        return self._salary
    
    def __str__(self) -> str:
        return super().__str__() + " \nField of Work: " + self._field_of_work + "\nSalary: " + str(self._salary)

if __name__ == "__main__":
    test_id = 1
    test_name = "Nave"
    test_age = 26

    try:
        employee = Employee(test_id, test_name, test_age)
    except ValueError:
        print("Error: Failed to create Employee instance due to invalid input.")
    else:
        if employee.getId() != test_id:
            printShouldBeError("ID", test_id, employee.getId())
        if employee.getName() != test_name:
            printShouldBeError("Name", test_name, employee.getName())
        if employee.getAge() != test_age:
            printShouldBeError("Age", test_age, employee.getAge())