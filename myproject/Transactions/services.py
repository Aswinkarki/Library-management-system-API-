from .repositories import TransactionRepository
from uuid import UUID

class TransactionService:
    def __init__(self):
        self.repository = TransactionRepository()

    def get_all_transactions(self):
        return self.repository.get_all_transactions()

    def get_transaction_by_id(self, transaction_id):
        return self.repository.get_transaction_by_id(transaction_id)

    def create_transaction(self, data):
        return self.repository.create_transaction(data)

    def update_transaction(self, transaction_id, data):
        return self.repository.update_transaction(transaction_id, data)

    def delete_transaction(self, transaction_id):
        return self.repository.delete_transaction(transaction_id)