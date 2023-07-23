from django.urls import path
from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.contrib.auth.forms import UserCreationForm
from stocks.models import Stock
from django.http import HttpResponse
from django.shortcuts import render,reverse
from stocks.forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin


# def stock_view(request):
#     context ={"stocks":Stock}
#     return render(request,"djcrm/stock_list.html",context)

class stock_view(LoginRequiredMixin,ListView):
    
    template_name = "djcrm/stock_list.html"
    queryset = Stock.objects.all()
    context_object_name = "stocks"

class sign_up_view(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    
    def get_success_url(self):
        return reverse("log-in")
    



