from django.urls import path
from .views import  MyTokenObtainPairView,getUserProfile,getAllProfile,userRegister

urlpatterns = [ 
    path("signup/",userRegister,name="register"),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path("user/profile/",getUserProfile,name="userProfile"),
    path("users",getAllProfile,name="users"),  
]