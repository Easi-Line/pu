# Initial balance
balance = 1000

# Function to check balance
def check_balance():
    print(f"Your balance is ${balance}")


# Function to deposit money
def withdraw(amount):
    global balance
    balance += amount
    print(f"Deposit succesful! Your new balance is ${balance}")

#Function to withdraw money
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"withdrawal successful! Your new balance is ${balance}")

# Main loop
print("Welcome to Easi Money!")
while True:
    action = input("Choose an action: check balance, deposit, withdraw, exit\n> ").lower() 
   