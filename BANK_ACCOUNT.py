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

    def get_balance(self):
        return self.balance

    def send_money(self, amount, receiver):
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self.transactions.append(f"Sent {amount} to {receiver.user_id}")
            receiver.transactions.append(f"Received {amount} from {self.user_id}")
            return True
        else:
            return False
