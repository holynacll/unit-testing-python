from src.bank.account import Conta


def processPayment(sender: Conta, recipient: Conta, amount: float):
    if sender.withdraw(amount):
        recipient.deposit(amount)
        print(f"Transferência de R$ {amount} realizada com sucesso!")
        sender.display()
        recipient.display()
