from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('prediction',views.prediction,name="prediction"),
    path('login',views.login,name="login"),
    path('predict_crop',views.predict_crop,name="predict_crop"),
    path('logout',views.logout,name="logout")
]