from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import stock_in_list_view,stock_in_deatil_view,stock_in_create_view,stock_in_update_view,stock_in_delete_view
from .views import stock_out_list_view,stock_out_deatil_view,stock_out_create_view,stock_out_update_view,stock_out_delete_view
app_name= "stocks"
urlpatterns=[
    path("in/",stock_in_list_view,name="in-list"),
    path("in/<int:pk>/",stock_in_deatil_view.as_view(),name = "in-detail"), 
    path("in/<int:pk>/update/",stock_in_update_view,name = "in-update"),
    path("in/<int:pk>/delete/",stock_in_delete_view,name = "in-delete"),
    path("in/create/",stock_in_create_view.as_view(),name = "in-create"),
    path("out/",stock_out_list_view,name="out-list"),
    path("out/<int:pk>/",stock_out_deatil_view.as_view(),name = "out-detail"), 
    path("out/<int:pk>/update/",stock_out_update_view,name = "out-update"),
    path("out/<int:pk>/delete/",stock_out_delete_view,name = "out-delete"),
    path("out/create/",stock_out_create_view,name = "out-create"),
]
