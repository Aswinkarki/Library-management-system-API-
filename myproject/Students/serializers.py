from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'student_id', 'student_name', 'email', 'contact_number', 'department', 
            'user', 'created_date', 'updated_date', 'is_deleted'
        ]
def validate(self, data):
        # Check if a student with the same email and user already exists
        email = data.get('email')
        user = data.get('user')
        if Student.objects.filter(email=email, user=user).exists():
            raise serializers.ValidationError("A student with this email already exists for the user.")
        return data