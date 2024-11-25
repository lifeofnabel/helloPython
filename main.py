from BANK import BANK
from USERS import USERS
from CASH_MASCHINE import CASH_MASCHINE
from BANK_ACCOUNT import BANK_ACCOUNT

bank = BANK("Sparkasse")
user = USERS("JAMILA", 1)
cash_machine = CASH_MASCHINE("Frankfurter Str. 0, 60333 FFM", "Sparkasse")
account = BANK_ACCOUNT("1","DE37", "SLS1", "n@n.de", 100, user )

print("Setup abgeschlossen!")
print(user.toString())
print(bank.toString())

