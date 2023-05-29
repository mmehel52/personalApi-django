
from django.urls import path
from .views import( DepartmentListCreateView,DepartmentRUDView,PersonnelListCreateView)

urlpatterns=[
    path('departments/',DepartmentListCreateView.as_view()),
    path('departments/<int:pk>/',DepartmentRUDView.as_view()),
    path('personels/',P)
]