from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.home,name='api.home'),
#     path('product/',include('api.product.urls')),
#     path('category/',include('api.category.urls')),
#     path('order/',include('api.order.urls')),
#     path('payment/',include('api.payment.urls')),
#     path('user/',include('api.user.urls')),
]