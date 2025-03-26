

from django.urls import path
from .views import train_list, book_ticket, ticket_list

urlpatterns = [
    path('', train_list, name='train_list'),  # Homepage should show train list
    path('book/<int:train_id>/', book_ticket, name='book_ticket'),
    path('tickets/', ticket_list, name='ticket_list'),
]
