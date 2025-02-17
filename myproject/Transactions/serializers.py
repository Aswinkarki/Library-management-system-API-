from rest_framework import serializers
from .models import TransactionModel
from Students.models import Student
from Users.models import User
from Books.models import Book
from uuid import UUID

class TransactionSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = TransactionModel
        fields = [
            'transaction_id', 'student', 'user', 'book', 
            'transaction_type', 'date'
        ]

    def validate(self, data):
        # Validate UUID for 'user' field
        if not isinstance(data['user'].pk, UUID):
            raise serializers.ValidationError({"user": "Invalid UUID format."})
        
        # Check if student and book exist (if their primary keys are integers)
        if not Student.objects.filter(pk=data['student'].pk).exists():
            raise serializers.ValidationError({"student": "Invalid student ID."})
        if not Book.objects.filter(pk=data['book'].pk).exists():
            raise serializers.ValidationError({"book": "Invalid book ID."})

        return data
