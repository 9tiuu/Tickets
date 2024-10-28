from django.contrib import admin
from django.urls import path
from tickets.views import TicketListView, TicketCreateView, TicketDetailView, TicketDeleteView, TicketUpdateView

urlpatterns = [
    path('', TicketListView.as_view(), name='list'),
    path('create/', TicketCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', TicketDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', TicketDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', TicketUpdateView.as_view(), name='update')
]
