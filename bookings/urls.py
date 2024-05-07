from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_page, name='test_page'),
    path('add_flight/', views.add_flight, name='add_flight'),
    path('flights/', views.flight_list, name='flight_list'),
    path('buy_ticket/<int:flight_id>/', views.buy_ticket, name='buy_ticket'),
    path('success/', views.success_page, name='success_page'),
]
