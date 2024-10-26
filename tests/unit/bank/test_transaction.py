from unittest.mock import MagicMock

from src.bank.memory_database import MemoryDatabase
from src.bank.account import Conta
from src.bank.transaction import processPayment, processPayment_with_db

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



def test_process_payment_saves_transaction():
    # Configurando contas de remetente e destinatário
    sender = Conta("Alice", 100)
    recipient = Conta("Bob", 50)

    # Mocking do banco de dados em memória
    db_mock = MagicMock(spec=MemoryDatabase)

    # Realizando a transferência
    processPayment_with_db(sender, recipient, 30, db_mock)

    # Verificando se a transação foi salva no banco de dados
    db_mock.save_transaction.assert_called_once_with("Alice", "Bob", 30)
