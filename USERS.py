from hellopython.BANK_ACCOUNT import BANK_ACCOUNT
from hellopython.main import account


class USERS:
    def __init__(self, name, id):
        self.name: str = name
        self.id: str = id
        self.accounts = []

    def add_user(self, user):
        self.users[user.id] = user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_all_users(self):
        return self.users

    def remove_user(self, user_id):
        del self.users[user_id]

    def update_user(self, user_id, user):
        self.users[user_id] = user

    def __str__(self):
        return str(self.users)

    def get_accounts(self):
        return self.accounts

    def create_new_account(self, iban, bic, email, start_balance):
        account: BANK_ACCOUNT = BANK_ACCOUNT(self.id, iban, bic, email, start_balance)
        self.accounts.append(account)
        return account

    def to_string(self):
        return f"User: {self.name}, ID: {self.id}, Accounts: {[account.to_string() for account in self.accounts]}"


