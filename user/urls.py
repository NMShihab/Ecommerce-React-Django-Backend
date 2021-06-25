from django.urls import path


from . import views

urlpatterns =[
    path('api/user/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/profile/', views.getUserProfile, name='user_profile'),

   
]