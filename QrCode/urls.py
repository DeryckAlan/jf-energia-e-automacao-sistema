from django.urls import path
from . import views

urlpatterns = [
    path('qrlist/', views.QRcodeList, name='qrlist'),
    path('qrcreate/', views.QRcodeCreate, name='qrform')
]
