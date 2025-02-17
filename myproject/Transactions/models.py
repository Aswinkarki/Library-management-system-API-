from django.db import models
import uuid
from Students.models import Student  
from Books.models import Book  
from Users.models import User  # Assuming you're using Django's built-in User model

class TransactionModel(models.Model):
    TRANSACTION_TYPES = [
        ('BORROW', 'Borrow'),
        ('RETURN', 'Return'),
    ]

    transaction_id = models.AutoField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # ForeignKey to Student model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to User model (managing the transaction)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # ForeignKey to Book model
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.book.title} by {self.student.name}"
