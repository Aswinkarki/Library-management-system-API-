from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from datetime import timedelta
from Students.models import Student
from Books.models import Book
from Transactions.models import TransactionModel

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_students = Student.objects.filter(is_deleted=False).count()
        total_books = Book.objects.filter(is_deleted=False).count()
        total_transactions = TransactionModel.objects.count()
        total_borrowed_books = TransactionModel.objects.filter(transaction_type="BORROW").count()
        total_returned_books = TransactionModel.objects.filter(transaction_type="RETURN").count()

        # Get overdue borrowers (assuming 7-day borrow period)
        overdue_days = 30
        overdue_borrowers = TransactionModel.objects.filter(
            transaction_type="BORROW",
            date__lte=now() - timedelta(days=overdue_days)
        ).select_related("student")

        overdue_list = [
            {"name": transaction.student.student_name, "borrowed_id": str(transaction.transaction_id)}
            for transaction in overdue_borrowers
        ]

        dashboard_data = {
            "total_student_count": total_students,
            "total_book_count": total_books,
            "total_transaction_count": total_transactions,
            "total_borrowed_books": total_borrowed_books,
            "total_returned_books": total_returned_books,
            "overdue_borrowers": overdue_list,
        }

        return Response(dashboard_data)
