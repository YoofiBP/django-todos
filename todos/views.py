from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.


class TodoIndex(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoShow(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
