from hellopython.BANK_ACCOUNT import BANK_ACCOUNT
class BANK:
    def __init__(self, name):
        self.name: str = name
        self.users = {}

    def add_user(self, user):
        self.users[user.id] = user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def counting_down(self):
        print("Closing bank accounts...")
        for user_id, user in self.users.items():
            for account in user.get_accounts():
                balance = account.get_balance()
                while balance > 0:
                    print(f"Closing {account.iban}: {balance}")
                    balance -= 1
        print("All accounts closed!")

    def to_string(self):
        return f"Bank: {self.name}, Users: {[user.to_string() for user in self.users.values()]}"