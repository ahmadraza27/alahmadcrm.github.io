"""
URL configuration for djcrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import stock_view,sign_up_view,stock_detail_view,stock_delete_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",stock_view,name='stocks-list'),
    path('stocks/<int:pk>/',stock_detail_view.as_view(),name="stocks-detail" ),
    path('stocks/<int:pk>/delete',stock_delete_view,name="stocks-delete" ),
    path('stocks/', include(("stocks.urls","stocks"),namespace="stocks")),
    path('login/', LoginView.as_view(),name="log-in"),
    path('logout/', LogoutView.as_view(),name="log-out"),
    path('signup/', sign_up_view.as_view(),name="sign-up"),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
