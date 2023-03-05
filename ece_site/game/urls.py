from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('setname/', views.setname),
    path('oauth/google', views.google_oauth),
    path('game/', views.gamePage),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('logout/', views.Logout),
    path('testu', views.testu),
]