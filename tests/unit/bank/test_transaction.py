from src.bank.account import Conta
from src.bank.transaction import processPayment

def test_deve_realizar_transferencia():
    # Arrange
    recipient = Conta("you", 20)
    sender = Conta("me", 150)

    # Act
    processPayment(sender, recipient, 100)
    
    # Assert
    assert sender.balance == 50
    assert recipient.balance == 120


def test_nao_deve_realizar_transacao():
    # Arrange
    recipient = Conta("you", 20)
    sender = Conta("me", 50)

    # Act
    processPayment(sender, recipient, 100)

    # Assert
    assert sender.balance == 50
    assert recipient.balance == 20
