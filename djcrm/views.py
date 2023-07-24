from django.urls import path
from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from django.contrib.auth.forms import UserCreationForm
from stocks.models import Stock
from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect
from stocks.forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# def stock_view(request):
#     context ={"stocks":Stock}
#     return render(request,"djcrm/stock_list.html",context)

@login_required
def stock_delete_view(request,pk):
    
    
    
    st= Stock.objects.get(id=pk)
    st.delete()
    
    
    
    return redirect("stocks-list")
    


# class stock_view(LoginRequiredMixin,ListView):
    
#     template_name = "djcrm/stock_list.html"
#     queryset = Stock.objects.all()
#     context_object_name = "stocks"


class stock_detail_view(LoginRequiredMixin,DetailView):
    
    template_name = "djcrm/stock_detail.html"
    queryset = Stock.objects.all()
    context_object_name = "object_detail"

@login_required()
def stock_view(request):
    
    object = Stock.objects.all()
    
    if request.method =="POST":
        cname=request.POST.get('company-name')
        tcode=request.POST.get('tile-code')
        tsize=request.POST.get('tile-size')
        
        bquantity=request.POST.get('box-quantity')
        bcapacity=request.POST.get('box-capacity')
        
        print(request.POST)
        if cname != ""  :
            object = object.filter(company_name__icontains=cname)
            context = {"stocks":object}
        
        if tcode != "":
            object = object.filter(tile_code__icontains=tcode)
            context = {"stocks":object}
        if tsize != "":
            object = object.filter(tile_size=tsize)
            context = {"stocks":object}
        if bquantity != "" and cname.isnumeric():
            object = object.filter(box_quantity__gt=bquantity)
            context = {"stocks":object}
        
        if bcapacity != "" and cname.isnumeric():
            object = object.filter(box_capacity=bcapacity)
            context = {"stocks":object}
        print("stock view called")
    context = {"stocks":object}

 
    return render(request,"djcrm/stock_list.html",context)

   


class sign_up_view(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    
    def get_success_url(self):
        return reverse("log-in")
    



