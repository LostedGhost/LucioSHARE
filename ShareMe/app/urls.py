from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('load', upload, name='upload'),
    path('view/<str:slug>', view, name='view')
]