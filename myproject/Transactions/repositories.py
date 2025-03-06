from .models import TransactionModel

class TransactionRepository:
    def __init__(self):
        self.model = TransactionModel

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, transaction_id):
        return self.model.objects.filter(transaction_id=transaction_id,is_deleted=False).first()

    def create(self, data):
        return self.model.objects.create(**data)

    def update(self, transaction_id, data):
        Transaction = self.get_by_id(transaction_id)
        if Transaction:
            for key, value in data.items():
                setattr(Transaction, key, value)
            Transaction.save()
        return Transaction

    def delete(self, transaction_id):
        Transaction = self.get_by_id(transaction_id)
        if Transaction:
            Transaction.delete()
            return True
        return False
