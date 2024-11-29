from django.urls import path
from . import views
app_name = 'management'
urlpatterns = [
    path('requests/', views.service_request_list,),
    path('requests/new/', views.service_request_create,),
]
