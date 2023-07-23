from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Stock_in,Stock_out
from .forms import stock_in_form,stock_out_form

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# stock_in list class based view 
class stock_in_list_view(LoginRequiredMixin,ListView):
    template_name = "stocks/in_list.html"
    queryset = Stock_in.objects.all()
    context_object_name = 'object_list'
def stock_in_list_view(request):
    object = Stock_in.objects.all()
    context = {"object_list":object}
    if request.method =="POST":
        cname=request.POST.get('company-name')
        tcode=request.POST.get('tile-code')
        
        bquantity=request.POST.get('box-quantity')
        byperson=request.POST.get('by-person')
        print(request.POST)
        if cname != "":
            object = object.filter(company_name__icontains=cname)
            context = {"object_list":object}
        
        if tcode != "":
            object = object.filter(tile_code__icontains=tcode)
            context = {"object_list":object}
        if bquantity != "":
            object = object.filter(box_quantity_in__gt=bquantity)
            context = {"object_list":object}
        
        if byperson != "":
            object = object.filter(by_person__person__username=byperson)
            context = {"object_list":object}
        


 
    return render(request,"stocks/in_list.html",context)

    
    
    
class stock_out_list_view(LoginRequiredMixin,ListView):
    template_name = "stocks/out_list.html"
    queryset = Stock_out.objects.all()
    context_object_name = 'object_list'



# stock_in deatil view of certain stock_in
class stock_in_deatil_view(LoginRequiredMixin,DetailView):
    template_name = "stocks/in_detail.html"
    queryset = Stock_in.objects.all()
    context_object_name = 'object_detail'
    
class stock_out_deatil_view(LoginRequiredMixin,DetailView):
    template_name = "stocks/out_detail.html"
    queryset = Stock_out.objects.all()
    context_object_name = 'object_detail'
    

# def stock_in_detail(request,pk):
#     context = {"stin":Stock_in.objects.get(id=pk)}
#     return render(request,"stocks/in_detail.html",context)
#     # return HttpResponse("hello")



class stock_in_create_view(LoginRequiredMixin,CreateView):
    template_name = "stocks/in_create.html"
    form_class = stock_in_form
    
    def get_success_url(self):
        return reverse("stocks:in-list")
    
class stock_out_create_view(LoginRequiredMixin,CreateView):
    template_name = "stocks/out_create.html"
    form_class = stock_out_form
    
    def get_success_url(self):
        return reverse("stocks:out-list")
    
class stock_in_update_view(LoginRequiredMixin,UpdateView):
    template_name = "stocks/in_update.html"
    form_class = stock_in_form
    queryset= Stock_in.objects.all()
    
    def get_success_url(self):
        return reverse("stocks:in-list")
    
    
class stock_out_update_view(LoginRequiredMixin,UpdateView):
    template_name = "stocks/out_update.html"
    form_class = stock_out_form
    queryset= Stock_out.objects.all()
    
    def get_success_url(self):
        return reverse("stocks:out-list")
    
    
# class stock_in_delete_view(DeleteView):
    
#     template_name='stocks/in_delete.html'
#     queryset= Stock_in.objects.all()
    
#     def get_success_url(self):
#         return reverse("stocks:in-list")
def stock_in_delete_view(LoginRequiredMixin,request,pk):
    
    
    
    st= Stock_in.objects.get(id=pk)
    st.delete()
    
    
    
    return redirect("stocks:in-list")
    
# class stock_out_delete_view(DeleteView):
    
#     template_name='stocks/out_delete.html'
#     queryset= Stock_out.objects.all()
    
#     def get_success_url(self):
#         return reverse("stocks:out-list")
    
def stock_out_delete_view(LoginRequiredMixin,request,pk):



    st= Stock_out.objects.get(id=pk)
    st.delete()



    return redirect("stocks:out-list")
# def stock_in_create_view(request):
#     form = stock_in_form()
#     if request.method == "POST":
#         form = stock_in_form(request.POST)
#         print("post-----------------")
#         if form.is_valid():
#             print("valid-----------------")
#             form.save()
#             return redirect("/stocks/in")
    
    
    
#     return render(request,"stocks/in_create.html",{"form":form})