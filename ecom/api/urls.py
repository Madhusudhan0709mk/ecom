
from django.urls import path,include
from . import views
# from rest_framework.authtoken import views

urlpatterns = [
    path('',views.home,name='home'),
    path('category/',include('api.category.urls')),
    path('product/',include('api.product.urls'))
]
