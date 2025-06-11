from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls')),  # Homepage and app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Login/logout/password URLs
]