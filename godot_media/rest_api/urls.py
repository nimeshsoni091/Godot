from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.partner_list),  # localhost:port/restApi/
]
