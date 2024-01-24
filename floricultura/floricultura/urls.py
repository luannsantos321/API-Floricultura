from django.contrib import admin
from django.urls import path, include
from flores.views import FloresAPIView, FlorAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('flores/', FloresAPIView.as_view(), name='flores'),
    path('flores/<int:pk>',FlorAPIView.as_view(), name='flor' )
   
]
