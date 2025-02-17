# from django.db import models
# from datetime import datetime

# class Dashboard(models.Model):
#     total_student_count = models.IntegerField(default=0)
#     total_book_count = models.IntegerField(default=0)
#     total_transaction_count = models.IntegerField(default=0)
#     total_borrowed_books = models.IntegerField(default=0)
#     total_returned_books = models.IntegerField(default=0)
#     recorded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the data was recorded

#     def __str__(self):
#         return f"Dashboard Stats at {self.recorded_at.strftime('%Y-%m-%d %H:%M:%S')}"
