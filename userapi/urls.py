from django.urls import path
from .views import  MyTokenObtainPairView,getUserProfile,getAllProfile,userRegister,updateUserProfile,deleteUser,adminEditProfile,adminDetailProfile

urlpatterns = [ 
    path("signup/",userRegister,name="register"),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path("user/profile/",getUserProfile,name="userProfile"),
    path("user/profile/update/",updateUserProfile,name="userProfileUpdate"),
    path("users",getAllProfile,name="users"), 
    path("delete/<str:pk>/",deleteUser,name='user-delete'),
    path("profile/update/<str:pk>/",adminEditProfile,name='profile-update'),
    path("profile/<str:pk>/",adminDetailProfile,name='profile'),
      
]