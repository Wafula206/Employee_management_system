from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee_list'),  # List all employees
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),  # Add new employee
    path('<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),  # Edit employee
     path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
   # path('home/', views.homepage, name='homepage'),  # Coming Soon (optional)
]
