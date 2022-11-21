from django.urls import path
from . import views

urlpatterns = [
    path('', views.locacaoList, name='locacao-list'),
    path('locacao/<int:id>', views.locacaoView, name='locacao-View'),
    path('newLocacao/', views.newLocacao, name="new-Locacao"),
]
