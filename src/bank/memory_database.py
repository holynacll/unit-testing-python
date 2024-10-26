# src/bank/account.py
class MemoryDatabase:
    def __init__(self):
        self.transactions = []

    def save_transaction(self, sender_name: str, recipient_name: str, amount: float):
        transaction = {
            "sender": sender_name,
            "recipient": recipient_name,
            "amount": amount
        }
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions