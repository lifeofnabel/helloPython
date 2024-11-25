from hellopython.BANK_ACCOUNT import BANK_ACCOUNT


class USERS:
    def __init__(self, name, id):
        self.users = {}
        self.name = name
        self.id = id

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

    def get_accounts(self, user_id):
        # return all accounts of the user from the list
        return self.users[user_id].accounts

    def createNewAccount(self, user, iban, bic, email, start_balance):
        # Create a new account
        # create new object of BANK_ACCOUNT
        # object of bank account needs a user_id, iban, bic, email, start_balance
        # add the object to the user
        # return the object
        account = BANK_ACCOUNT.BANK_ACCOUNT(user.id, iban, bic, email, start_balance)
        user.add_account(account)
        return account

    def toString(self):
        return self.name, self.id, self.users
        pass


