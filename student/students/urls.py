                                    # APIView
from django.urls import path
# from .views import StudentList, StudentCreate, StudentRetrieve, StudentUpdate, StudentDelete

# urlpatterns = [
#     path('students/', StudentList.as_view(), name='student_list'),
#     path('students/create/', StudentCreate.as_view(), name='student_create'),
#     path('students/<int:pk>/', StudentRetrieve.as_view(), name='student_detail'),
#     path('students/update/<int:pk>/', StudentUpdate.as_view(), name='student_update'),
#     path('students/delete/<int:pk>/', StudentDelete.as_view(), name='student_delete'),
# ]


                                     # viewsets 
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
urlpatterns = router.urls