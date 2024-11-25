# Class for bank account
class BANK_ACCOUNT:

    def __init__(self, user_id, iban, bic, email, start_balance, user):
        self.user_id = user_id
        self.iban = iban
        self.bic = bic
        self.email = email
        self.balance = start_balance
        self.transactions = []

    @classmethod
    def BANK_ACCOUNT(cls, id, iban, bic, email, start_balance):
        pass
