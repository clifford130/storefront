from django.urls import path
from .import views

# urls config
urlpatterns = [
    # path('', views.playground_home, name='playground_home'),
    path('', views.say_hello)
]
