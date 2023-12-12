# physio_game/urls.py
from django.contrib import admin
from django.urls import path
from physio_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('emailsaving', views.email),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('game_selection/', views.game_selection, name='game_selection'),
    path('physio_category/', views.physio_category, name='physio_category'),
    path('physio_category/General_Wellness/', views.general_well),
    path('physio_category/Cardiac', views.cardiac),
    path('physio_category/Falls_Prevention', views.fall_prevention),
    path('physio_category/Orthopedic', views.orthopedic)
]
