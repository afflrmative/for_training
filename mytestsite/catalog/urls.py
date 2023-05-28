from django.urls import path, re_path
from . import views



urlpatterns = [
    path('',views.index, name='index'),
    path('games/', views.GamesListView.as_view(), name='games'),
    path('game/<int:pk>', views.GamesDetailView.as_view(), name="game-detail"),
    path('companys/', views.CompanysListView.as_view(), name='companys'),
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name='company-detail'),
    path('mygames/', views.AddedGamesByUserListView.as_view(), name='my-borrowed'),
]