from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.partner_form, name='partner_insert'),  # localhost:port/partner
    path('<int:id>/', views.partner_form, name='partner_update'),
]
