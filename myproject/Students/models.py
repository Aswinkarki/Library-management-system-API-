from django.db import models
import uuid
from Users.models import User

class Student(models.Model):
    student_id = models.AutoField(primary_key=True, editable=False)
    student_name = models.CharField(max_length=255, default="Unknown Student")
    email = models.EmailField(unique=True)  # No default here
    contact_number = models.CharField(max_length=15, default="0000000000")
    department = models.CharField(max_length=255, default="Undeclared")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students', default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
    # Generate a unique email if it's not provided
     if not self.email:
        self.email = f"student_{uuid.uuid4()}@domain.com"  # Use UUID for uniqueness
    
    # Ensure email is unique by checking and updating it if necessary
     attempt = 1
     while Student.objects.filter(email=self.email).exists():
        self.email = f"student_{uuid.uuid4()}@domain.com"  # Regenerate with new UUID
        attempt += 1
        if attempt > 10:  # Limit the number of retries to prevent an infinite loop
            raise ValueError("Unable to generate a unique email after multiple attempts")
    
     super().save(*args, **kwargs)
    def __str__(self):
        return self.student_name
