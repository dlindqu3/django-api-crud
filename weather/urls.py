from django.urls import path 
from . import views

urlpatterns = [
  # base url /weather/
  path('api/', views.get_weather, name='get_weather'),
  path('weather-list/', views.weather_list, name='weather-list'),
  # GET /weather/weather-detail/2
   path('weather-detail/<str:pk>/', views.weather_detail, name='weather-detail'),
   path('weather-create/', views.weather_create, name='weather-create'),
   # /weather/weather-update/2/
   path('weather-update/<str:pk>/', views.weather_update, name='weather-update'),
   # go to route, then press "delete" button
   # this can be handled automatically from frontend 
   path('weather-delete/<str:pk>/', views.weather_delete, name='weather-delete'),
   path('weather-create-query/<str:query>', views.make_api_call_and_weather_create, name='weather-create-query'),
]
