from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeForm

#admin profile view
from django.contrib.auth.decorators import login_required, user_passes_test
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_profile(request):
    return render(request, 'employees/admin_profile.html')
#homepage

from django.shortcuts import render

def homepage(request):
    return render(request, 'employees/homepage.html')

def about(request):
    return render(request, 'employees/about.html')

def events(request):
    return render(request, 'employees/events.html')

def employee_portal(request):
    return render(request, 'employees/employee_portal.html')

def contact(request):
    return render(request, 'employees/contact.html')


class EmployeeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Employee
    template_name = 'employees/employee_list.html'  # fixed path
    context_object_name = 'object_list'  # so {% for employee in object_list %} works

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class EmployeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'  # fixed path
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class EmployeeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'  # fixed path
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class EmployeeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser