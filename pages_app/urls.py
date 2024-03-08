from django.urls import path, include
from .views import index,uz,eng,ru
urlpatterns = [
    path('weekdays',index,name='main'),
    path('weekdays/uz',uz,name='uz'),
    path('weekdays/eng',eng,name='eng'),
    path('weekdays/ru',ru,name='ru')
]

# app in urls 