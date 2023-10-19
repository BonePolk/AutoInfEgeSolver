class Theme:
    def __init__(self, theme_id, amount):
        self.id = theme_id
        self.amount = amount

    def __repr__(self):
        return f"(Theme {self.id} with {self.amount} problems)"
