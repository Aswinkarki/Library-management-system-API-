from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Books.services import BookService
from rest_framework.permissions import IsAuthenticated
from uuid import UUID
from Books.serializers import BookSerializer
from Authors.models import Author

class BookListView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get(self, request):
        service = BookService()
        books = service.get_all_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
     data = request.data.copy()  # Create a mutable copy of request.data
     author_id = data.get('author')
     try:
        author_id = int(author_id)  # Ensure it's a valid integer
        author = Author.objects.get(author_id=author_id)  # Use author_id instead of id
     except (ValueError, Author.DoesNotExist):
        return Response({'error': 'Invalid or non-existent author ID'}, status=status.HTTP_400_BAD_REQUEST)

     data['author'] = author.author_id  # Use author_id instead of id

    # Validate and save the book
     serializer = BookSerializer(data=data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get(self, request, book_id):
        service = BookService()
        book = service.get_book_by_id(book_id)
        if book:
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, book_id):
        service = BookService()
        data = request.data
        book = service.update_book(book_id, data)
        if book:
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, book_id):
        service = BookService()
        book = service.delete_book(book_id)
        if book:
            return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)