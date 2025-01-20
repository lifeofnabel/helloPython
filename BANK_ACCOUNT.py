class BANK_ACCOUNT:
    def __init__(self, user, iban, bic, email, start_balance):
        self.user = user
        self.iban = iban
        self.bic = bic
        self.email = email
        self.balance = start_balance
        self.transactions = []  # Initialize transactions as an empty list

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def send_money(self, amount: float, receiver: "BANK_ACCOUNT") -> bool:
        """
        Send money to another account.
        Updates balances and transaction logs for both accounts.
        """
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self.transactions.append(f"Sent {amount} to {receiver.iban}")
            receiver.transactions.append(f"Received {amount} from {self.iban}")
            return True
        else:
            print("No enough Money!")
            return False

    def add_transaction(self, description: str):
        """Add a transaction description."""
        self.transactions.append(description)

    def to_string(self) -> str:
        """Return a string representation of the account details and transactions."""
        return (f"IBAN: {self.iban}, BIC: {self.bic}, Email: {self.email}, "
                f"Balance: {self.balance}, Transactions: {self.transactions}")
