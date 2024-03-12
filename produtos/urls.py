from django.urls import path
from . import views 


urlpatterns = [
    path('<int:id>/', views.produtos_view, name="detalhe_produto"),
    path('', views.home_view),
]
