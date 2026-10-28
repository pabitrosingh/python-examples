"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

try:
  result = 10/0
except Exception as ex:
  print(f"Exception: {ex}")   
else:
  # Executes ONLY if the try block succeeds without errors
  print(f"Success! The result is: {result}")
finally:
  # ALWAYS executes, no matter what (useful for cleanup tasks)
  print("Division attempt finished.\n")

print("----raise error------")
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age successfully set to: {age}")
# --- Testing the code ---
try:
    set_age(-5) 
except ValueError as error:
    print(f"Caught an error: {error}")

print("--------Custom Exception----------")
#Define the custom exception class
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Attempted to withdraw ₹{amount}, but balance is only ₹{balance}.")


def withdraw_money(balance, amount):
    if amount > balance:
        # Trigger the custom error
        raise InsufficientFundsError(balance, amount)
        
    new_balance = balance - amount
    print(f"Withdrawal successful! New balance: ₹{new_balance}")
    return new_balance

# Handle the custom exception
try:
    current_balance = 500
    withdraw_money(current_balance, 600)
    
except InsufficientFundsError as error:
    # Access custom attributes inside the exception block
    print(f"Transaction Denied: {error}")
    print(f"Shortage amount: ₹{error.amount - error.balance}")