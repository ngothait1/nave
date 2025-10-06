import os
import pandas as pd

from utils import printNotNumerError, printNotStringError
from Person import Person
from Student import Student
from Employee import Employee
from menu_actions import Action

def saveNewEntry(persons_dict: dict[int: Person], ids_list: list[int], data_list: list[dict[str: any]], sum_of_ages: int) -> int:
    id = input("Enter ID: ")
    if not id.isdigit():
        printNotNumerError("ID", id)
        return sum_of_ages
    id = int(id)

    if id in persons_dict:
        print(f"Error: ID '{id}' already exists.")
        return sum_of_ages

    name = input("Enter Name: ")
    if name.isdigit():
        printNotStringError("Name", name)
        return sum_of_ages
    
    age = input("Enter Age: ")
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
    menu_text = "Choose an option:\n"
    for i, cls in enumerate(person_types):
        menu_text += f"{i}. {cls.__name__}\n"
    menu_text += f"Enter your choice (0-{len(person_types) - 1}): "
    choice = input(menu_text).strip()
    if not choice.isdigit():
        printNotNumerError("Choice", choice)
        return False
    choice = int(choice)

    if choice < 0 or choice > len(person_types) - 1:
        print("Error: Option [" + str(choice) + "] doesn't exist.")
        return False

    try:
        entry = person_types[choice](id, name, age)
    except ValueError:
        return False
    
    persons_dict[id] = entry
    data_list.append(entry.getObjectAsCSV())

    return True

def searchById(persons_dict: dict[int: Person]) -> None:
    id = input("Plese enter the ID you want to look for: ")
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
    index = input("Plese enter the index of the entry you want to print: ")
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
    file_name = input("What is your output file name? ")
    df = pd.DataFrame(data_list)
    df.to_csv(os.getcwd() + "/" + file_name)
    print("The data saved successfully.")

def exitFunc() -> None:
    while True:
        choice = input("Are you sure? (y/n) ").strip().lower()
        if choice == "y":
            print("Goodbye!")
            return False
        elif choice == "n":
            return True

def menu() -> None:
    for action in Action:
        option_text = action.name.replace("_", " ").title()
        print(f"{action.value}. {option_text}")

def main() -> None:
    persons_dict = {}
    ids_list = []
    data_list = []
    sum_of_ages = 0
    running = True

    # Functions that perform side-effects and/or update sum_of_ages / running
    def doSaveNewEntry() -> None:
        nonlocal sum_of_ages
        sum_of_ages = saveNewEntry(persons_dict, ids_list, data_list, sum_of_ages)

    def doExitFunc() -> None:
        nonlocal running
        running = exitFunc()

    # Dispatcher: map an Enum action to the corresponding function
    dispatch = {
        Action.SAVE_NEW_ENTRY:          doSaveNewEntry,
        Action.SEARCH_BY_ID:            lambda: searchById(persons_dict),
        Action.PRINT_AGES_AVG:          lambda: printAgesAverage(persons_dict, sum_of_ages),
        Action.PRINT_ALL_NAMES:         lambda: printAllNames(persons_dict),
        Action.PRINT_ALL_IDS:           lambda: printAllIds(ids_list),
        Action.PRINT_ALL_ENTRIES:       lambda: printAllEntries(persons_dict),
        Action.PRINT_ENTRY_BY_INDEX:    lambda: printEntryByIndex(persons_dict, ids_list),
        Action.SAVE_ALL_DATA:           lambda: saveAllData(data_list),
        Action.EXIT:                    doExitFunc,
    }

    while running:
        menu()

        try:
            choice = input("Please enter your choice: ").strip()
            action = Action(int(choice))    # immediate conversion from number → Enum
            dispatch[action]()  # invoke according to the dictionary

            if running:
                input("Press Enter to continue")
        except ValueError:
            print(f"Option [{choice}] doesn't exist. Please try again.")
        except KeyboardInterrupt:
            print("\nUser interrupted with Ctrl+C, exiting...")
            running = False

if __name__ == "__main__":
    main()