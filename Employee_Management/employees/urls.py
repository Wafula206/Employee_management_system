from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage with links
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),  # List all employees
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),  # Add new employee
    path('<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),  # Edit employee
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('employee-portal/', views.employee_portal, name='employee_portal'),
    path('admin/profile/', views.admin_profile, name='admin_profile'),  # if you have this view
    path('contact/', views.contact, name='contact'),
    path('admin-profile/', views.admin_profile, name='admin_profile'),
]