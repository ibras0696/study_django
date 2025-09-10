from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Новый маршрут для главной страницы блога
    path('about/', views.about, name='about'),  # Новый маршрут для страницы "О блоге",
    path('contact/', views.contact, name='contact'), # Новый маршрут для страницы "Контакты",
    path('old-home/', views.old_home, name='old_home'), # Новый маршрут для старой главной страницы блога
    path('old-home-it-ansar/', views.old_home_it_ansar, name='old_home_it_ansar'), # Новый маршрут для представления с HTML файлом
    path('new-home-it-ansar/', views.new_home_it_ansar, name='new_home_it_ansar'), # Новый маршрут для представления с HTML файлом
    path('project/', views.project_ansar, name='project_ansar'), # Новый маршрут для представления с HTML файлом
    path('team/', views.team_ansar, name='team_ansar'), # Новый маршрут для представления с HTML файлом
    path('contacts/', views.contact, name='contact'), # Новый маршрут для представления с HTML файлом
    path('index/', views.index, name='index'), # Новый маршрут для представления с передачей контекста
    path('profile/', views.profile, name='profile'), # Новый маршрут для представления с передачей контекста
]