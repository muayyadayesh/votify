from django.urls import path
from .views import *

#Defining global app name
app_name = 'votingapp'

#Polls urlPatterns
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('polls/', poll_list.as_view(), name='poll_list'),
    path('polls/new/', create_poll.as_view(), name='create_poll'),
    path('polls/<int:pk>/', pull_details.as_view(), name='pull_details'),
    path('polls/<int:pk>/vote', poll_vote.as_view(), name='poll_vote'),
    path('polls/<int:pk>/result', poll_result.as_view(), name='poll_result'),
]
