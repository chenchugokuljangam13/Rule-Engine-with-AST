# from django.urls import path
# from .views import add_rule, evaluate

# urlpatterns = [
#     path('add_rule/', add_rule, name='add_rule'),
#     path('evaluate/', evaluate, name='evaluate'),
# ]


from django.urls import path
from .views import home, evaluate

urlpatterns = [
    path('', home, name='home'),  # This serves your main HTML page
    path('api/evaluate/', evaluate, name='evaluate'),  # This is the API endpoint for rule evaluation
]