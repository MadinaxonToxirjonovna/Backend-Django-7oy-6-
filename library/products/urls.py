from django.urls import path
from .views import BookList, BookCreate,  BookUpdate, BookDelete, BookDetail#, BookListCreate, BookRetrieveDestroy, 

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('create/', BookCreate.as_view(), name='create_book'),
    path('delete/<int:pk>/', BookDelete.as_view(), name='delete_book'),
    path('detail/<int:pk>/', BookDetail.as_view(), name='detail_book'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='update_book'),
]




# from .views import BookViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'books', BookViewSet, basename='book')
# urlpatterns = router.urls