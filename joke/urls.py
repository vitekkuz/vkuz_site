from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='main_page'),  #
    path('<int:jokeid>/', randomjoke, name='random_joke'),  #

]

