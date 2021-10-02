from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('event/', views.EventList.as_view(), name='event'),
    path('event/<int:pk>/', views.EventDetail.as_view()),
]