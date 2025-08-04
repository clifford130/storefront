from django.urls import path
from .import views

# urls config
urlpatterns = [
    path('', views.playground_home, name='playground_home'),
    path('hello/', views.say_hello)
]
