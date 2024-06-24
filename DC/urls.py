from django.urls import path
from DC.views import *
app_name='something'

urlpatterns=[
    path('panth/',panth,name='panth'),
 
]