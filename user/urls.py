from django.urls import path


from . import views

urlpatterns =[
    path('api/user/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/register/', views.registerUser, name='register_user'),
    path('user/profile/', views.getUserProfile, name='user_profile'),
    path('users/', views.getUsers, name='users'),

   
]