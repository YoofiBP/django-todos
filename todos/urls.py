from django.urls import path
from .views import TodoIndex, TodoShow

urlpatterns = [
    path('', TodoIndex.as_view()),
    path('<int:pk>/', TodoShow.as_view()),
]
