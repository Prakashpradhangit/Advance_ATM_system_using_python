import os  # Import the os module to check for file existence

# Define a constant for the PIN code
pin = 1234

def get_balance():
    """
    Retrieves the balance from the 'a.txt' file.
    If the file doesn't exist or contains invalid data, returns 0.
    """
    if os.path.exists("a.txt"):
        with open("a.txt", "r") as f:
            try:
                balance = int(f.read().strip())  # Convert the file content to an integer
                return balance
            except ValueError:
                return 0  # Return 0 if the file contains non-integer data
    return 0  # Return 0 if the file doesn't exist

def update_balance(balance):
    """
    Writes the current balance to the 'a.txt' file.
    """
    with open("a.txt", "w") as f:
        f.write(str(balance))  # Write the balance as a string to the file

def check_balance():
    """
    Prompts the user for their PIN and, if correct, displays their balance.
    """
    pas = int(input("Enter pin: "))
    if pas == pin:
        balance = get_balance()  # Retrieve the current balance
        print(f"Your balance is {balance}")
    else:
        print("Wrong pin")  # Notify the user if the PIN is incorrect

def deposit_cash():
    """
    Prompts the user for their PIN and deposit amount, updates the balance if the PIN is correct.
    """
    pas = int(input("Enter pin: "))
    if pas == pin:
        deposit = int(input("Enter amount to deposit: "))
        balance = get_balance()  # Retrieve the current balance
        balance += deposit  # Add the deposit amount to the balance
        update_balance(balance)  # Update the balance in the file
        print(f"Your money {deposit} successfully deposited. Updated balance is {balance}.")
    else:
        print("Wrong pin")  # Notify the user if the PIN is incorrect

def withdraw_cash():
    """
    Prompts the user for their PIN and withdrawal amount, updates the balance if the PIN is correct and funds are sufficient.
    """
    pas = int(input("Enter pin: "))
    if pas == pin:
        withdraw = int(input("Enter amount to withdraw: "))
        balance = get_balance()  # Retrieve the current balance
        if balance >= withdraw:
            balance -= withdraw  # Deduct the withdrawal amount from the balance
            update_balance(balance)  # Update the balance in the file
            print(f"Your money {withdraw} successfully withdrawn. Updated balance is {balance}.")
        else:
            print("Insufficient balance")  # Notify the user if they don't have enough funds
    else:
        print("Wrong pin")  # Notify the user if the PIN is incorrect

def main():
    """
    Main function to run the ATM program.
    Presents a menu for the user to check balance, deposit cash, withdraw cash, or exit.
    """
    while True:
        print("\nMenu")
        print("1. Check balance")
        print("2. Deposit cash")
        print("3. Withdraw cash")
        print("4. Exit")
        
        option = int(input("Enter choice: "))
        
        if option == 1:
            check_balance()  # Check the balance
        elif option == 2:
            deposit_cash()  # Deposit cash
        elif option == 3:
            withdraw_cash()  # Withdraw cash
        elif option == 4:
            print("Exiting...")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice")  # Handle invalid menu choices

if __name__ == "__main__":
    main()  # Run the main function
