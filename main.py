from BANK import BANK
from USERS import USERS
from CASH_MASCHINE import CASH_MASCHINE
from BANK_ACCOUNT import BANK_ACCOUNT

bank = BANK("Sparkasse")
print("Bank erstellt!")
user = USERS("JAMILA", 1)
print("User erstellt!")
user2 = USERS("JAMIL", 2)
print("User2 erstellt!")

user.createNewAccount(user, "DE37", "SLS1", "n@g", 100)
print("Account erstellt!")
user2.createNewAccount(user2, "DE73", "SLS2", "j@j", 200)
print("Account2 erstellt!")

account2 = user2.get_accounts(2)
print("Account2 gegettet: ", account2)
print("Account2 Balance: ", account2.balance)
account = user.get_accounts(1)
print("Account gegettet: ", account)
print("Account Balance: ", account.balance)


print("Setup abgeschlossen!")
print(user.toString())
print(bank.toString())

