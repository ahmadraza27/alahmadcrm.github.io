from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Stock_in,Stock_out,Stock
from .forms import stock_in_form,stock_out_form

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

# stock_in list class based view 
# class stock_in_list_view(LoginRequiredMixin,ListView):
#     template_name = "stocks/in_list.html"
#     queryset = Stock_in.objects.all()
#     context_object_name = 'object_list'

@login_required
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
        if bquantity != "" and bquantity.isnumeric():
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
    
@login_required
def stock_out_list_view(request):
    object = Stock_out.objects.all()
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
        if bquantity != "" and bquantity.isnumeric():
            object = object.filter(box_quantity_out__gt=bquantity)
            context = {"object_list":object}
        
        if byperson != "":
            object = object.filter(by_person__person__username=byperson)
            context = {"object_list":object}
        


 
    return render(request,"stocks/out_list.html",context)



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
    
@login_required
def stock_out_create_view(request):
    form = stock_out_form()
    object = Stock.objects.all()
    if request.method=="POST":
        form = stock_out_form(request.POST)
        if form.is_valid():
            
            # print(form.cleaned_data['by_person'])
            out_company_name=form.cleaned_data['company_name']
            out_tile_code=form.cleaned_data['tile_code']
            out_tile_size=form.cleaned_data['tile_size']
            # out_tile_picture=form.cleaned_data['tile_picture']
            out_box_quantity=form.cleaned_data['box_quantity_out']
            out_box_capacity=form.cleaned_data['box_capacity']
            out_by_person=form.cleaned_data['by_person']
            
            object = object.filter(company_name__icontains=out_company_name)
            
    
        
            object = object.filter(tile_code__icontains=out_tile_code)
            
        
            object = object.filter(box_capacity=out_box_capacity)
            
        
        
            object = object.filter(tile_size=out_tile_size)
            count_ = object.count() > 0
#             {'company_name': 'master', 'tile_code': '123', 'tile_size': '12x12', 'tile_picture': None, 'box_quantity_out': 12, 'box_capacity': 1.44, 'by_person': 
# <Person: ahmad>}
            if count_ and object[0].box_quantity > 0:
                print("obejct-----------")
                form.save() 
                return render(request,"stocks/out_list.html",{"object_list":Stock_out.objects.all()})
                
    
            
            
    context={"form":form}
    return render(request,"stocks/out_create.html",context)
    
    
class stock_in_update_view(LoginRequiredMixin,UpdateView):
    template_name = "stocks/in_update.html"
    form_class = stock_in_form
    queryset= Stock_in.objects.all()
    
    def get_success_url(self):
        return reverse("stocks:in-list")
    
def stock_in_update_view(request,pk):
    st  = Stock_in.objects.get(id=pk)
    q = st.box_quantity_in
    cn = st.company_name
    tc = st.tile_code
    ts= st.tile_size
    bc= st.box_capacity
    object = Stock.objects.all()
    print(q)
    object = object.get(company_name=cn,tile_code=tc,box_capacity=bc,tile_size=ts)
    print(object)
    form = stock_in_form(instance=st)
    if request.method=="POST":
        object.box_quantity -= q
        object.save()
        form = stock_in_form(request.POST,instance=st)
        if form.is_valid():
            print(form.cleaned_data['box_quantity_in'],"cleaned data =============")
            form.save()
            return render(request,"stocks/in_detail.html",{'object_detail':Stock_in.objects.get(id=pk)})
    context = {'form':form}
    return render(request,"stocks/in_update.html",context)
    
    
class stock_out_update_view(LoginRequiredMixin,UpdateView):
    template_name = "stocks/out_update.html"
    form_class = stock_out_form
    queryset= Stock_out.objects.all()
    
    def get_success_url(self):
        return reverse("stocks:out-list")


def stock_out_update_view(request,pk):
    st  = Stock_out.objects.get(id=pk)
    q = st.box_quantity_out
    cn = st.company_name
    tc = st.tile_code
    ts= st.tile_size
    bc= st.box_capacity
    object = Stock.objects.all()
    print(q)
    object = object.get(company_name=cn,tile_code=tc,box_capacity=bc,tile_size=ts)
    print(object)
    form = stock_out_form(instance=st)
    if request.method=="POST":
        object.box_quantity += q
        object.save()
        form = stock_out_form(request.POST,instance=st)
        if form.is_valid():
            print(form.cleaned_data['box_quantity_out'],"cleaned data =============")
            form.save()
            return render(request,"stocks/out_detail.html",{'object_detail':Stock_out.objects.get(id=pk)})
    context = {'form':form}
    return render(request,"stocks/out_update.html",context)
     
    
# class stock_in_delete_view(DeleteView):
    
#     template_name='stocks/in_delete.html'
#     queryset= Stock_in.objects.all()
    
#     def get_success_url(self):
#         return reverse("stocks:in-list")

@login_required
def stock_in_delete_view(request,pk):
    
    
    
    st= Stock_in.objects.get(id=pk)
    st.delete()
    
    
    
    return redirect("stocks:in-list")
    
# class stock_out_delete_view(DeleteView):
    
#     template_name='stocks/out_delete.html'
#     queryset= Stock_out.objects.all()
    
#     def get_success_url(self):
#         return reverse("stocks:out-list")
    
@login_required
def stock_out_delete_view(request,pk):



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