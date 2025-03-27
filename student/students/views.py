                                         # APIView
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from .models import Student
# from .serializers import StudentSerializer

# class StudentList(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response({"data": serializer.data, "status": status.HTTP_200_OK, "message": "Students List"})

# class StudentCreate(APIView):
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "message": "Student Created"})
#         return Response({"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

# class StudentRetrieve(APIView):
#     def get(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student)
#         return Response({"data": serializer.data, "status": status.HTTP_200_OK, "message": "Student Details"})

# class StudentUpdate(APIView):
#     def put(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"data": serializer.data, "status": status.HTTP_200_OK, "message": "Student Updated"})
#         return Response({"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

#     def patch(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"data": serializer.data, "status": status.HTTP_200_OK, "message": "Student Partially Updated"})
#         return Response({"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

# class StudentDelete(APIView):
#     def delete(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         student.delete()
#         return Response({"message": "Student Deleted"}, status=status.HTTP_204_NO_CONTENT)


                                      # viewsets 
from.models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'


