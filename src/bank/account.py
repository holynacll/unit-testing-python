class Conta:
    """A simple Account for a Banking App"""
    def __init__(self, name: str, initial_balance=0):
        self.name = name
        self.balance = initial_balance
    
    def deposit(self, amount: float) -> float:
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount: float) -> float:
        if self.is_valid_operation(amount):
            self.balance -= amount
            return True
        return False
    
    def is_valid_operation(self, amount: float) -> bool:
        if 0 < amount <= self.balance:
            return True
    
    def display(self) -> float:
        print(f"Account holder: {self.name}")
        print(f"Account balance: ${self.balance:.2f}")
        return self.balance
        