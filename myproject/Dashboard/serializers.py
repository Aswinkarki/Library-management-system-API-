# from rest_framework import serializers
# from Students.models import Student
# from Books.models import Book
# from Transactions.models import TransactionModel


# class OverdueBorrowerSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     borrowed_id = serializers.CharField()


# class DashboardSerializer(serializers.Serializer):
#     total_student_count = serializers.IntegerField()
#     total_book_count = serializers.IntegerField()
#     total_transaction_count = serializers.IntegerField()
#     total_borrowed_books = serializers.IntegerField()
#     total_returned_books = serializers.IntegerField()
#     overdue_borrowers = OverdueBorrowerSerializer(many=True)
