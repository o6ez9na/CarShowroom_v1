from typing import Any
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import *

# Create your views here.


class CarShowroomListView(ListView):
    model = CarShowroom
    template_name = "car_showrooms.html"
    context_object_name = "car_s"


class CarShowroomDetailView(DetailView):
    model = CarShowroom
    template_name = "detail.html"
    context_object_name = "detail"


class AutoListView(ListView):
    model = Automobile
    template_name = "auto.html"
    context_object_name = "auto"


class AutoDetailView(DetailView):
    model = Automobile
    template_name = "auto_detail.html"
    context_object_name = "auto_detail"


class SaleListView(ListView):
    model = Sale
    template_name = "sale.html"
    context_object_name = "sale"


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sale_details.html"
    context_object_name = "sale_detail"


class AssistantListView(ListView):
    model = ShopAssistant
    template_name = "assistants.html"
    context_object_name = "assistant"


class AssistantDetailView(DetailView):
    model = ShopAssistant
    template_name = "assistants_details.html"
    context_object_name = "assistants_details"


class BrandsListView(ListView):
    model = Brand
    template_name = "brands.html"
    context_object_name = "brands"


class BrandsDetailView(DetailView):
    model = Brand
    template_name = "brands_details.html"
    context_object_name = "brands_details"


class ClientsListView(ListView):
    model = Client
    template_name = "clients.html"
    context_object_name = "clients"


class ClientsDetailView(DetailView):
    model = Client
    template_name = "clients_details.html"
    context_object_name = "clients_details"


# Клиенты
class ClientCreateView(CreateView):
    model = Client
    template_name = "edit_page.html"
    form_class = ClientForm
    success_url = reverse_lazy("edit_page")

    def get_context_data(self, **kwargs: Any):
        kwargs["list_params"] = Client.objects.all().order_by("id")
        return super().get_context_data(**kwargs)


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "edit_page.html"
    form_class = ClientForm
    success_url = reverse_lazy("edit_page")

    def get_context_data(self, **kwargs: Any):
        kwargs["update"] = True
        return super().get_context_data(**kwargs)


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "edit_page.html"
    success_url = reverse_lazy("edit_page")

# продажи
class SaleCreateView(CreateView):
    model = Sale
    template_name = "edit_page_sale.html"
    form_class = SaleForm
    success_url = reverse_lazy("edit_page_sale")

    def get_context_data(self, **kwargs: Any):
        kwargs["list_params"] = Sale.objects.all().order_by("id")
        return super().get_context_data(**kwargs)

class SaleUpdateView(UpdateView):
    model = Sale
    template_name = "edit_page_sale.html"
    form_class = SaleForm
    success_url = reverse_lazy("edit_page_sale")

    def get_context_data(self, **kwargs: Any):
        kwargs["update"] = True
        return super().get_context_data(**kwargs)

class SaleDeleteView(DeleteView):
    model = Sale
    template_name = "edit_page_sale.html"
    success_url = reverse_lazy("edit_page_sale")


# Ассистенты
class AssistantCreateView(CreateView):
    model = ShopAssistant
    template_name = "edit_page_assistant.html"
    form_class = AssistantForm
    success_url = reverse_lazy("edit_page_assistant")

    def get_context_data(self, **kwargs: Any):
        kwargs["list_params"] = ShopAssistant.objects.all().order_by("id")
        return super().get_context_data(**kwargs)

class AssistantUpdateView(UpdateView):
    model = ShopAssistant
    template_name = "edit_page_assistant.html"
    form_class = AssistantForm
    success_url = reverse_lazy("edit_page_assistant")

    def get_context_data(self, **kwargs: Any):
        kwargs["update"] = True
        return super().get_context_data(**kwargs)

class AssistantDeleteView(DeleteView):
    model = ShopAssistant
    template_name = "edit_page_assistant.html"
    success_url = reverse_lazy("edit_page_assistant")

# Автомобиль
class AutoCreateView(CreateView):
    model = Automobile
    template_name = "edit_page_auto.html"
    form_class = AutoForm
    success_url = reverse_lazy("edit_page_auto")

    def get_context_data(self, **kwargs: Any):
        kwargs["list_params"] = Automobile.objects.all().order_by("id")
        return super().get_context_data(**kwargs)

class AutoUpdateView(UpdateView):
    model = Automobile
    template_name = "edit_page_auto.html"
    form_class = AutoForm
    success_url = reverse_lazy("edit_page_auto")

    def get_context_data(self, **kwargs: Any):
        kwargs["update"] = True
        return super().get_context_data(**kwargs)
    
class AutoDeleteView(DeleteView):
    model = Automobile
    template_name = "edit_page_auto.html"
    success_url = reverse_lazy("edit_page_auto")


# Бренд
class BrandsCreateView(CreateView):
    model = Brand
    template_name = "edit_page_brands.html"
    form_class = BrandForm
    success_url = reverse_lazy("edit_page_brands")

    def get_context_data(self, **kwargs: Any):
        kwargs["list_params"] = Brand.objects.all().order_by("id")
        return super().get_context_data(**kwargs)

class BrandUpdateView(UpdateView):
    model = Brand
    template_name = "edit_page_brands.html"
    form_class = BrandForm
    success_url = reverse_lazy("edit_page_brands")

    def get_context_data(self, **kwargs: Any):
        kwargs["update"] = True
        return super().get_context_data(**kwargs)

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = "edit_page_brands.html"
    success_url = reverse_lazy("edit_page_brands")

# Автосалоны
class ShowroomCreateView(CreateView):
    model = CarShowroom
    template_name = "edit_page_showrooms.html"
    form_class = CarShowroomForm
    success_url = reverse_lazy("edit_page_showrooms")

    def get_context_data(self, **kwargs: Any):
        kwargs["list_params"] = CarShowroom.objects.all().order_by("id")
        return super().get_context_data(**kwargs)

class ShowroomUpdateView(UpdateView):
    model = CarShowroom
    template_name = "edit_page.html"
    form_class = CarShowroomForm
    success_url = reverse_lazy("edit_page_showrooms")

    def get_context_data(self, **kwargs: Any):
        kwargs["update"] = True
        return super().get_context_data(**kwargs)

class ShowroomDeleteView(DeleteView):
    model = CarShowroom
    template_name = "edit_page_showrooms.html"
    success_url = reverse_lazy("edit_page_showrooms")
    
# Логин
class LogoutPageView(LogoutView):
    next_page = reverse_lazy('login')
    
class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('car_s')
    
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid
        
class LoginPageView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('car_s')
    def get_success_url(self):
        return self.success_url