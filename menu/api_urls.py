from django.urls import path
from .import views
app_name = 'menu'
urlpatterns = [
    path('GetFormation', views.api_get_formations),
]
