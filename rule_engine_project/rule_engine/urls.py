from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page to display test cases
    path('add_test_case/', views.add_test_case, name='add_test_case'),  # Endpoint for adding a new test case
]
