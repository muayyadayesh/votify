from django.urls import path
from .views import *

#Defining global app name
app_name = 'votingapp'

#Polls urlPatterns
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('poll/', poll_list.as_view(), name='poll_list'),
    path('poll/<int:pk>/', poll_details.as_view(), name='poll_details'),
    path('poll/new/', poll_create.as_view(), name='poll_create'),
    path('poll/<int:pk>/delete', poll_delete.as_view(), name='poll_delete'),
    path('poll/<int:pk>/update_poll', poll_update.as_view(), name='poll_update'),
    path('poll/<int:pk>/vote', poll_vote.as_view(), name='poll_vote'),
    path('poll/<int:pk>/result', poll_vote.as_view(), name='poll_result'),
]
