from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import StudentService
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated

class StudentListCreateView(APIView):
    """Handles listing and creating students."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        students = StudentService.get_students_by_user(request.user)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Get data from request body
        data = request.data

        # Get the authenticated user instance (this is the currently authenticated user)
        user_instance = request.user  # This is already the User instance from the authentication

        # Assign the user instance to the data dictionary
        data['user'] = user_instance

        try:
            # Call the service to create a student
            student = StudentService.create_student(data)
            if student:
                # Use the serializer to convert the student object into JSON
                student_data = StudentSerializer(student).data
                return Response(student_data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Error creating student"}, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    """Handles retrieving, updating, and deleting a student."""
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        student = StudentService.get_student(student_id)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, student_id):
        student = StudentService.get_student(student_id)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            updated_student = StudentService.update_student(student_id, serializer.validated_data)
            return Response(StudentSerializer(updated_student).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, student_id):
        success = StudentService.delete_student(student_id)
        if success:
            return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
