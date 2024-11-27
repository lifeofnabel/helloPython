# Class for bank account
class BANK_ACCOUNT:

    def __init__(self, user_id, iban, bic, email, start_balance, user):
        self.user_id = user_id
        self.iban: int = iban
        self.bic: str = bic
        self.email: str = email
        self.balance: float = start_balance
        self.transactions = []

    @classmethod
    def BANK_ACCOUNT(cls, id, iban, bic, email, start_balance):
        pass
