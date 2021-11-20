from django.urls import path
from .views import *

#Defining global app name
app_name = 'votingapp'

#Polls urlPatterns
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('poll/', poll_list.as_view(), name='poll_list'),
    path('poll/<int:pk>/', poll_details.as_view(), name='poll_details'),
    path('poll/poll_new/', newpoll, name='poll_new'),
    path('poll/<int:pk>/poll_delete', poll_delete.as_view(), name='poll_delete'),
    path('poll/<int:pk>/poll_update', poll_update.as_view(), name='poll_update'),
    path('poll/<int:pk>', poll_result.as_view(), name='poll_result'),
    path('poll/<int:pk>/poll_vote', poll_vote.as_view(), name='poll_vote'),
    path('poll/<int:pk>/answer', poll_vote_action, name='poll_vote_action'),
]
