from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('produtos/',include('produtos.urls')),
    path('admin/', admin.site.urls),
]
