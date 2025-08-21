import time

def even_or_odd(num1, num2):
    even1 = True
    even2 = True

    line = "even."
    if num1 % 2 != 0:
        line = "odd."
        even1 = False
    print("I can see that the first number is " + line)

    line = "even."
    if num2 % 2 != 0:
        line = "odd."
        even2 = False
    print("And the second number is " + line)
    
    line = "So both of them are "
    if even1 and even2:
        print(line + "even.")
    elif not even1 and not even2:
        print(line + "odd.")
    else:
        print("So one of them is even, and one is odd.")

def calculator(num1, num2):
    flag = True
    operator = input("Operator (+, -, *, /): ")
    result = 0
    line = "An error had occured, please try again later."

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        answer = input("You chose division, should the result be integer? (y/n) ")
        if num2 != 0:
            if answer == 'y':
                result = num1 // num2
            else:
                result = num1 / num2
        else:
            print("Error: num_2 is zero.\n" + line)
            flag = False
    else:
        print("Error: Operator " + operator + " is not supported.\n" + line)
        flag = False

    if flag:
        print(str(num1) + " " + operator + " " + str(num2) + " = " + str(round(result, 2)))

def main():
    print("Hello, This is my final project!")

    name = input("What is your name? ")
    print("Hi " + name + ", nice to meet you!\nThis is a special calculator, I would need two numbers from you.")

    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    print("Thank you for putting in your numbers, " + str(num1) + " and " + str(num2) + ".")

    even_or_odd(num1, num2)

    calculator(num1, num2)

    print("Thank you " + name + "for using the calculator on" + " " + time.ctime() + ".")

main()