from Person import Person
from utils import printNotNumerError, printNotStringError, printShouldBeError

class Student(Person):
    def __init__(self, id: int, name: str, age: int) -> None:
        super().__init__(id, name, age)

        try:
            self._field_of_study = input("Enter Field of Study: ")
        except KeyboardInterrupt:
            print("\nUser interrupted with Ctrl+C, exiting...")
            raise KeyError()
        if self._field_of_study.isdigit():
            printNotStringError("Field of Study", self._field_of_study)
            raise ValueError()
        
        try:
            year_of_study = input("Enter Year of Study: ")
        except KeyboardInterrupt:
            print("\nUser interrupted with Ctrl+C, exiting...")
            raise KeyError()
        if not year_of_study.isdigit():
            printNotNumerError("Year of Study", year_of_study)
            raise ValueError()
        self._year_of_study = int(year_of_study)

        try:
            gpa = input("Enter GPA: ")
        except KeyboardInterrupt:
            print("\nUser interrupted with Ctrl+C, exiting...")
            raise KeyError()
        if not gpa.isdigit():
            printNotNumerError("GPA", gpa)
            raise ValueError()
        self._gpa = float(gpa)

    def getFieldOfStudy(self) -> str:
        return self._field_of_study
    
    def getYearOfStudy(self) -> int:
        return self._year_of_study
    
    def getGPA(self) -> float:
        return self._gpa
    
    def __str__(self) -> str:
        return super().__str__() + " \nField of Study: " + self._field_of_study + \
            "\nYear of Study: " + str(self._year_of_study) + "\nGPA: " + str(self._gpa)

if __name__ == "__main__":
    test_id = 1
    test_name = "Nave"
    test_age = 26

    try:
        student = Student(test_id, test_name, test_age)
    except ValueError:
        print("Error: Failed to create Student instance due to invalid input.")
    else:
        if student.getId() != test_id:
            printShouldBeError("ID", test_id, student.getId())
        if student.getName() != test_name:
            printShouldBeError("Name", test_name, student.getName())
        if student.getAge() != test_age:
            printShouldBeError("Age", test_age, student.getAge())