# Employee_Management/urls.py

from django.contrib import admin
from django.urls import path, include  # 👈 include is important

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls')),  # 👈 This connects the homepage
    path('accounts/', include('django.contrib.auth.urls')),  # <-- Add this line
]
