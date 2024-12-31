from hellopython.BANK_ACCOUNT import BANK_ACCOUNT


class USERS:
    def __init__(self, name: str, user_id: str):
        self.name: str = name
        self.id: str = user_id
        self.accounts: list[BANK_ACCOUNT] = []  # List to store user accounts

    def add_user(self, user: "USERS") -> None:
        """Add a user to the list."""
        self.accounts.append(user)

    def get_user(self, user_id: str) -> "USERS | None":
        """Retrieve a user by their ID."""
        return next((user for user in self.accounts if user.id == user_id), None)

    def get_all_users(self) -> list["USERS"]:
        """Retrieve all users."""
        return self.accounts

    def remove_user(self, user_id: str) -> None:
        """Remove a user by their ID."""
        self.accounts = [user for user in self.accounts if user.id != user_id]

    def update_user(self, user_id: str, user: "USERS") -> None:
        """Update user information."""
        for i, u in enumerate(self.accounts):
            if u.id == user_id:
                self.accounts[i] = user

    def get_accounts(self) -> list[BANK_ACCOUNT]:
        """Retrieve all accounts for this user."""
        return self.accounts

    def create_new_account(self, iban: str, bic: str, email: str, start_balance: float) -> BANK_ACCOUNT:
        """Create and add a new bank account."""
        account = BANK_ACCOUNT(self, iban, bic, email, start_balance)  # Pass 'self' as the user
        self.accounts.append(account)
        return account


    def create_new_account_with_params(self, iban: str, bic: str, email: str, start_balance: float) -> BANK_ACCOUNT:
        """Alternative method to create a new account with parameters."""
        return self.create_new_account(iban, bic, email, start_balance)

    def to_string(self) -> str:
        """Represent user details as a string."""
        return f"User: {self.name}, ID: {self.id}, Accounts: {[account.to_string() for account in self.accounts]}"
