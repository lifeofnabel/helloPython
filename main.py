from BANK import BANK
from USERS import USERS
from CASH_MASCHINE import CASH_MASCHINE
from BANK_ACCOUNT import BANK_ACCOUNT

# Create a bank instance
bank = BANK("Sparkasse")
print("Bank created!")

# Create users
user = USERS("JAMILA", 1)
print("User created!")
user2 = USERS("JAMIL", 2)
print("User2 created!")

# Create accounts for users
account1 = user.create_new_account("DE37", "SLS1", "n@g", 100)
print("Account created for User 1!")
account2 = user2.create_new_account("DE73", "SLS2", "j@j", 200)
print("Account created for User 2!")

# Add users to the bank
bank.add_user(user)
bank.add_user(user2)

# Retrieve specific accounts
retrieved_account1 = user.get_accounts()[0]
print("Retrieved Account 1:", retrieved_account1.to_string())
print("Account 1 Balance:", retrieved_account1.balance)

retrieved_account2 = user2.get_accounts()[0]
print("Retrieved Account 2:", retrieved_account2.to_string())
print("Account 2 Balance:", retrieved_account2.balance)

# Display setup summary
print("Setup completed!")
print(user.to_string())
print(bank.to_string())

# Perform counting_down task
print("Task: Counting Down")
bank.counting_down()
