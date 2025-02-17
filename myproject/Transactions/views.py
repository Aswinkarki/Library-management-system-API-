from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from Books.models import Book
from Students.models import Student
from Users.models import User
from .services import TransactionService
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from uuid import UUID

class TransactionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = TransactionService()
        transactions = service.get_all_transactions()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
    # Validate and create the transaction using the serializer
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
        # If data is valid, create the transaction
          transaction = serializer.save()
          return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
    
    # If serializer is invalid, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TransactionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, transaction_id):
        service = TransactionService()
        transaction = service.get_transaction_by_id(transaction_id)
        if transaction:
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, transaction_id):
        service = TransactionService()
        data = request.data
        transaction = service.update_transaction(transaction_id, data)
        if transaction:
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, transaction_id):
        service = TransactionService()
        transaction = service.delete_transaction(transaction_id)
        if transaction:
            return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)