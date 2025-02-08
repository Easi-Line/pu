import math

def get_numbers():
    num1 = float(input("Type your first number here: "))
    num2 = float(input("Type your second number here: "))
    return num1, num2

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def square_root(num1):
    return math.sqrt(num1)

def main():
    title = "skillup project"
    print(title.upper())

    choice = input("What mathematical operation do you want to work with? "
                   "(a) addition, (b) subtraction, (c) multiplication, (d) division, (e) square root: ")

    if choice == 'a':
        print("You have chosen the addition operator!!".upper())
        num1, num2 = get_numbers()
        result = addition(num1, num2)
    elif choice == 'b':
        print("You have chosen the subtraction operator!!".upper())
        num1, num2 = get_numbers()
        result = subtraction(num1, num2)
    elif choice == 'c':
        print("You have chosen the multiplication operator!!".upper())
        num1, num2 = get_numbers()
        result = multiplication(num1, num2)
    elif choice == 'd':
        print("You have chosen the division operator!!".upper())
        num1, num2 = get_numbers()
        result = division(num1, num2)
    elif choice == 'e':
        print("You have chosen the square root operation!!".upper())
        num1 = float(input("Type your number here: "))
        result = square_root(num1)
    else:
        print('Your input is not valid! Please enter a valid data type.')
        return

    print("The result of your input is " + str(result))

    feedback = input("Hope I helped you out? ")

    if feedback.lower() in ['yes', 'y']:
        print('Great!!! I will be available anytime you need me. Have a nice day. Buh-Bye for now.')
    elif feedback.lower() in ['no', 'n']:
        print('I am sorry but I am not a human and I do not assume for human,'
              'I was created to interpret simple arithmetics,'
              'so please review your question and let me help you.'
              'You can call 0257485575 for assistance. Thanks for your understanding')

if __name__ == "__main__":
    while True:
        main()
        restart = input("Do you want to perform another calculation? (yes/no): ").lower()
        if restart not in ['yes', 'y']:
            print("Goodbye!")
            break