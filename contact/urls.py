from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<message_id>', views.view_single_message, name='view_single_message'),
]
