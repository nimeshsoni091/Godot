from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pid>/', views.member_form, name='member_insert'),  # localhost:port/member
    path('<int:pid>/<int:id>/', views.member_form, name='member_update'),
    path('list/<int:id>', views.member_list, name='member_list'),
    path('delete/<int:id>', views.member_delete, name='member_delete')
]
