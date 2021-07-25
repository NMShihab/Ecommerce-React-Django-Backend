from django.urls import path

from . import views

urlpatterns =[
    path('products/',views.getProducts ,name='products'),
    path('products/<str:pk>/',views.getProduct,name='product'), 
    path('add/',views.addOrderItems,name="order-items"),
    path('order/<str:pk>',views.getOrderById,name="order"),
    path('order/<str:pk>/pay',views.updateOrderToPaid,name="pay"),
]