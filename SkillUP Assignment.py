print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
Option = int(input("Choose an operation: "))
if(Option in [1,2,3,4]):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if(Option == 1):
        result = num1 + num2
    elif(Option == 2):
        result = num1 - num2
    elif(Option == 3):
        result = num1 * num2
    elif(Option == 4):
        result = num1 / num2

else:
    print("Invalid operation entered")

print("The result of the operation {}".format(result))