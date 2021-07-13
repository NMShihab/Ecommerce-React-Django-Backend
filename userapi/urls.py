from django.urls import path
from .views import  MyTokenObtainPairView,getUserProfile,getAllProfile,userRegister,updateUserProfile

urlpatterns = [ 
    path("signup/",userRegister,name="register"),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path("user/profile/",getUserProfile,name="userProfile"),
    path("user/profile/update/",updateUserProfile,name="userProfileUpdate"),
    path("users",getAllProfile,name="users"),  
]