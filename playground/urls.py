from django.urls import path
from .import views

# urls config
urlpatterns = [
    path('hello/', views.say_hello)
]
