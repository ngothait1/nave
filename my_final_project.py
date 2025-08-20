import time

def even_or_odd(num1, num2):
    even1 = True
    even2 = True

    if num1 % 2 == 0:
        print("I can see that the first number is even.")
    else:
        print("I can see that the first number is odd.")
        even1 = False

    if num2 % 2 == 0:
        print("And the second is even.")
    else:
        print("And the second is odd.")
        even2 = False

    if even1 and even2:
        print("So both of them are even.")
    elif not even1 and not even2:
        print("So both of them are odd.")
    else:
        print("So one of them is even, and one is odd.")

def cal(num1, num2):
    flag = True
    op = input("Operator (+, -, *, /): ")
    res = 0

    if op == "+":
        res = num1 + num2
    elif op == "-":
        res = num1 - num2
    elif op == "*":
        res = num1 * num2
    elif op == "/":
        answer = input("You chose division, should the result be integer? (y/n) ")
        if num2 != 0:
            if answer == 'y':
                res = num1 // num2
            else:
                res = num1 / num2
        else:
            print("Error: num_2 is zero.")
            print("An error had occured, please try again later.")
            flag = False
    else:
        print("Error: Operator " + op + " is not supported.")
        print("An error had occurred, please try again later.")
        flag = False

    if flag:
        print(str(num1) + " " + op + " " + str(num2) + " = " + str(round(res, 2)))

def main():
    print("Hello, This is my final project!")

    name = input("What is your name? ")
    print("Hi " + name + ", nice to meet you!")
    print("This is a special calculator, I would need two numbers from you.")

    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    print("Thank you for putting in your numbers, " + str(num1) + " and " + str(num2) + ".")

    even_or_odd(num1, num2)

    cal(num1, num2)

    print("Thank you " + name + "for using the calculator on" + " " + time.ctime() + ".")

main()