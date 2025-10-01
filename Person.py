from utils import printShouldBeError

class Person:
    def __init__(self, id: int, name: str, age: int) -> None:
        self._id = id
        self._name = name
        self._age = age

    def getId(self) -> int:
        return self._id
    
    def getName(self) -> str:
        return self._name
    
    def getAge(self) -> int:
        return self._age
    
    def __str__(self) -> str:
        return "ID: " + str(self._id) + "\nName: " + self._name + "\nAge: " + str(self._age)

if __name__ == "__main__":
    test_id = 1
    test_name = "Nave"
    test_age = 26
    person = Person(test_id, test_name, test_age)

    if person.getId() != test_id:
        printShouldBeError("ID", test_id, person.getId())
    if person.getName() != test_name:
        printShouldBeError("Name", test_name, person.getName())
    if person.getAge() != test_age:
        printShouldBeError("Age", test_age, person.getAge())