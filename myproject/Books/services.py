from Books.repositories import BookRepository
from uuid import UUID

class BookService:
    def __init__(self):
        self.repository = BookRepository()  # Instantiate the repository class
    
    def get_all_books(self):
        return self.repository.get_all_books()

    def get_book_by_id(self, book_id):
        return self.repository.get_book_by_id(book_id)

    def create_book(self, data):
        return self.repository.create_book(data)

    def update_book(self, book_id, data):
        return self.repository.update_book(book_id, data)

    def delete_book(self, book_id):
        return self.repository.delete_book(book_id)