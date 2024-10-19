from django.urls import path
from .views import add_rule, evaluate

urlpatterns = [
    path('add_rule/', add_rule, name='add_rule'),
    path('evaluate/', evaluate, name='evaluate'),
]
