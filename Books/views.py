from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import BookSerializer
from .models import Book


class BookListView(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer

