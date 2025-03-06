from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer
from .services import TransactionService
from rest_framework.permissions import IsAuthenticated,AllowAny
from core.utils import handle_error

class TransactionListView(APIView):
    permission_classes = [AllowAny]

    @handle_error  # Decorator for handling errors
    def get(self, request):
        service = TransactionService()
        transactions = service.get_all_Transactions()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @handle_error
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()
            return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetailView(APIView):
    permission_classes = [AllowAny]

    @handle_error
    def get(self, request, transaction_id):
        service = TransactionService()
        transaction = service.get_Transaction_by_id(transaction_id)
        if transaction:
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

    @handle_error
    def put(self, request, transaction_id):
        service = TransactionService()
        data = request.data
        transaction = service.update_Transaction(transaction_id, data)
        if transaction:
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

    @handle_error
    def delete(self, request, transaction_id):
        service = TransactionService()
        transaction = service.delete_Transaction(transaction_id)
        if transaction:
            return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
