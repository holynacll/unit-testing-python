from src.bank.account import Conta
from src.bank.memory_database import MemoryDatabase

db = MemoryDatabase()

def processPayment(sender: Conta, recipient: Conta, amount: float):
    if sender.withdraw(amount):
        recipient.deposit(amount)
        print(f"Transferência de R$ {amount} realizada com sucesso!")
        sender.display()
        recipient.display()


def processPayment_with_db(sender: Conta, recipient: Conta, amount: float, db: MemoryDatabase = db):
    if sender.withdraw(amount):
        recipient.deposit(amount)
        db.save_transaction(sender.name, recipient.name, amount)
        print(f"Transferência de R$ {amount} realizada com sucesso!")
        sender.display()
        recipient.display()
