import os
import pandas as pd

from utils import printNotNumerError, printNotStringError
from Person import Person
from Student import Student
from Employee import Employee
from menu_actions import Action

running = True

def saveNewEntry(persons_dict: dict[int: Person], ids_list: list[int], data_list: list[dict[str: any]], sum_of_ages: int) -> int:
    global running

    try:
        id = input("Enter ID: ")
    except KeyboardInterrupt:
        print("\nUser interrupted with Ctrl+C, exiting...")
        running = False
        return sum_of_ages
    
    if not id.isdigit():
        printNotNumerError("ID", id)
        return sum_of_ages
    id = int(id)

    if id in persons_dict:
        print(f"Error: ID '{id}' already exists.")
        return sum_of_ages

    try:
        name = input("Enter Name: ")
    except KeyboardInterrupt:
        print("\nUser interrupted with Ctrl+C, exiting...")
        running = False
        return sum_of_ages
    
    if name.isdigit():
        printNotStringError("Name", name)
        return sum_of_ages
    
    try:
        age = input("Enter Age: ")
    except KeyboardInterrupt:
        print("\nUser interrupted with Ctrl+C, exiting...")
        running = False
        return sum_of_ages
    
    if not age.isdigit():
        printNotNumerError("Age", age)
        return sum_of_ages
    age = int(age)

    if not setDetails(persons_dict, data_list, id, name, age):
        return sum_of_ages

    ids_list.append(id)
    sum_of_ages += age

    print("ID [" + str(id) + "] saved successfully.")

    return sum_of_ages

def setDetails(persons_dict: dict[int: Person], data_list: list[dict[str: any]], id: int, name: str, age: int) -> bool:
    person_types = [Student, Employee, Person]
    global running
    
    try:
        choice = input(
            "Choose an option:\n"
            "0. Student\n"
            "1. Employee\n"
            "2. Neither\n"
            "Enter your choice (0/1/2): "
        ).strip()
    except KeyboardInterrupt:
        print("\nUser interrupted with Ctrl+C, exiting...")
        running = False
        return False
    
    if not choice.isdigit():
        printNotNumerError("Choice", choice)
        return False
    choice = int(choice)

    if choice < 0 or choice > 2:
        print("Error: Option [" + str(choice) + "] doesn't exist.")
        return False

    try:
        entry = person_types[choice](id, name, age)
    except ValueError:
        return False
    except KeyError:
        running = False
        return False
    
    persons_dict[id] = entry
    row = {
        "ID": id, "Name": name, "Age": age,
        "Field of Study": None, "Year of Study": None, "GPA": None,
        "Field of Work": None, "Salary": None,
    }

    if choice == 0:
        row.update({
            "Field of Study": entry.getFieldOfStudy(),
            "Year of Study": entry.getYearOfStudy(),
            "GPA": entry.getGPA(),
        })
    elif choice == 1:
        row.update({
            "Field of Work": entry.getFieldOfWork(),
            "Salary": entry.getSalary(),
        })

    data_list.append(row)

    return True

def searchById(persons_dict: dict[int: Person]) -> None:
    global running
    try:
        id = input("Plese enter the ID you want to look for: ")
    except KeyboardInterrupt:
        print("\nUser interrupted with Ctrl+C, exiting...")
        running = False
        return
    
    if not id.isdigit():
        printNotNumerError("ID", id)
        return
    id = int(id)

    if id not in persons_dict:
        print("Error: ID " + str(id) + " is not saved.")
        return
    
    print(persons_dict[id])

def printAgesAverage(persons_dict: dict[int: Person], sum_of_ages: int) -> None:
    size = len(persons_dict)
    if size == 0:
        print("0")
    else:
        avg = sum_of_ages / size
        print(f"{avg:.2f}")

def printAllNames(persons_dict: dict[int: Person]) -> None:
    for i, person in enumerate(persons_dict.values()):
        print(f"{i}. {person.getName()}")

def printAllIds(ids_list: list[int]) -> None:
    for i, id in enumerate(ids_list):
        print(f"{i}. {id}")

def printAllEntries(persons_dict: dict[int: Person]) -> None:
    for i, person in enumerate(persons_dict.values()):
        print(f"{i}. {person}")

def printEntryByIndex(persons_dict: dict[int: Person], ids_list: list[int]) -> None:
    global running
    try:
        index = input("Plese enter the index of the entry you want to print: ")
    except KeyboardInterrupt:
        print("\nUser interrupted with Ctrl+C, exiting...")
        running = False
        return
    
    if not index.isdigit():
        printNotNumerError("Index", index)
        return
    
    index = int(index)

    size = len(ids_list)
    if index < 0 or index >= size:
        print("Error: Index out of range. The maximum index allowed is " + str(size - 1))
        return
    
    id = ids_list[index]
    print(persons_dict[id])

def saveAllData(data_list: list[dict[str: any]]) -> None:
    global running
    try:
        file_name = input("What is your output file name? ")
    except KeyboardInterrupt:
        print("\nUser interrupted with Ctrl+C, exiting...")
        running = False
        return
    df = pd.DataFrame(data_list)
    df.to_csv(os.getcwd() + "/" + file_name)
    print("The data saved successfully.")

def exitFunc() -> None:
    global running
    while True:
        try:
            choice = input("Are you sure? (y/n) ").strip().lower()
        except KeyboardInterrupt:
            print("\nUser interrupted with Ctrl+C, exiting...")
            running = False
            return
        if choice == "y":
            print("Goodbye!")
            running = False
            return
        elif choice == "n":
            running = True
            return

def menu() -> None:
    options = [
        "Save a new entry",
        "Search by ID",
        "Print ages average",
        "Print all names",
        "Print all IDs",
        "Print all entries",
        "Print entry by index",
        "Save All Data",
        "Exit"
    ]

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def main() -> None:
    persons_dict = {}
    ids_list = []
    data_list = []
    sum_of_ages = 0
    global running

    # פעולות שעושות side-effects
    # ו/או מעדכנות sum_of_ages
    def doSaveNewEntry() -> None:
        nonlocal sum_of_ages
        sum_of_ages = saveNewEntry(persons_dict, ids_list, data_list, sum_of_ages)

    # dispatcher: ממפים פעולה מה - Enum
    # לפונקציה המתאימה
    dispatch = {
        Action.SAVE_NEW_ENTRY:      doSaveNewEntry,
        Action.SEARCH_BY_ID:        lambda: searchById(persons_dict),
        Action.PRINT_AGES_AVG:      lambda: printAgesAverage(persons_dict, sum_of_ages),
        Action.PRINT_ALL_NAMES:     lambda: printAllNames(persons_dict),
        Action.PRINT_ALL_IDS:       lambda: printAllIds(ids_list),
        Action.PRINT_ALL_ENTRIES:   lambda: printAllEntries(persons_dict),
        Action.PRINT_ENTRY_BY_IDX:  lambda: printEntryByIndex(persons_dict, ids_list),
        Action.SAVE_ALL_DATA:       lambda: saveAllData(data_list),
        Action.EXIT:                exitFunc,
    }

    while running:
        menu()

        try:
            choice = input("Please enter your choice: ").strip()
            action = Action(int(choice))    # המרה מיידית למספר → Enum
        except ValueError:
            print(f"Option [{choice}] doesn't exist. Please try again.")
        except KeyboardInterrupt:
            print("\nUser interrupted with Ctrl+C, exiting...")
            running = False
        else:
            dispatch[action]()  # הפעלה לפי המילון
            
        if running:
            try:
                input("Press Enter to continue")
            except KeyboardInterrupt:
                print("\nUser interrupted with Ctrl+C, exiting...")
                running = False

if __name__ == "__main__":
    main()