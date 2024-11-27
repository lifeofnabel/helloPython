class BANK:
    def __init__(self, name):
        self.name: str = name
        self.users = {}  # Benutzer speichern mit ID als Schlüssel

    def add_user(self, user):
        self.users[user.id] = user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def to_string(self):
        return f"Bank: {self.name}, Users: {[user.to_string() for user in self.users.values()]}"
