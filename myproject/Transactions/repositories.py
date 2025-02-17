from django.db import transaction
from uuid import UUID
from .models import TransactionModel
from Students.models import Student  # Import the Student model
from Users.models import User  # Import the User model
from Books.models import Book  # Import the Book model

class TransactionRepository:
    def __init__(self):
        self.model = TransactionModel

    def get_all_transactions(self):
        return self.model.objects.select_related('student', 'user_id', 'book').all()  # Optimized query

    def get_transaction_by_id(self, transaction_id):
        try:
            return self.model.objects.select_related('student', 'user_id', 'book').get(transaction_id=transaction_id)
        except TransactionModel.DoesNotExist:
            return None

    def create_transaction(self, data):
        with transaction.atomic():
            student = Student.objects.get(student_id=data['student'])
            user = User.objects.get(userId=data['user'])  # Ensure the field name is consistent
            book = Book.objects.get(book_id=data['book'])

            transaction_obj = self.model.objects.create(
                student=student,
                user=user,  # Make sure this is not 'user_id'
                book=book,
                transaction_type=data['transaction_type'],
            )
            return transaction_obj

    def update_transaction(self, transaction_id, data):
        try:
            transaction_obj = self.model.objects.get(transaction_id=transaction_id)
            transaction_obj.student = Student.objects.get(student_id=data.get('student', transaction_obj.student))
            transaction_obj.user_id = User.objects.get(userId=data.get('user_id', transaction_obj.user_id))
            transaction_obj.book = Book.objects.get(book_id=data.get('book', transaction_obj.book))
            transaction_obj.transaction_type = data.get('transaction_type', transaction_obj.transaction_type)
            transaction_obj.save()
            return transaction_obj
        except (TransactionModel.DoesNotExist, Student.DoesNotExist, User.DoesNotExist, Book.DoesNotExist):
            return None

    def delete_transaction(self, transaction_id):
        try:
            transaction_obj = self.model.objects.get(transaction_id=transaction_id)
            transaction_obj.delete()
            return transaction_obj
        except TransactionModel.DoesNotExist:
            return None