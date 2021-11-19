from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .models import *
from .forms import *

# Create your views here.

#Homepage
class home(TemplateView):
    template_name = 'home.html'

#List of all polls
class poll_list(TemplateView):
    model = Poll
    template_name = 'poll_list.html'
    def get_context_data(self, **kwargs):
        LastPolls = Poll.objects.filter(created_date__lte = timezone.now()).order_by('-created_date')
        TopPolls = Poll.objects.filter(last_update__lte = timezone.now()).order_by('-last_update')[:3]

        context_data = super().get_context_data(**kwargs)
        context_data['LastPolls'] = LastPolls
        context_data['TopPolls'] = TopPolls
        return context_data

#View poll details by the author: LoginRequired
class poll_details(LoginRequiredMixin, DetailView):
    model = Poll
    template_name = 'poll_details.html'

#Create new poll: LoginRequired
class poll_new( CreateView):
    template_name = 'poll_new.html'
    form_class = PollForm
    model = Poll

    # login_url = '/login'
    # redirect_field_name = 'votingapp/poll_details.html'

#Update the poll: LoginRequired
class poll_update(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'votingapp/poll_details.html'

    form_class = PollForm
    model = Poll

#Delete poll using deleteview: LoginRequired
class poll_delete(LoginRequiredMixin, DeleteView):
    model = Poll
    success_url = reverse_lazy('app:poll_list')

#Poll result, appears after voting action
class poll_result(DetailView):
    model = Poll
    template_name = 'poll_result.html'

#No auth required here
def poll_vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    form = VoteForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('votingapp:poll_result', pk=poll.pk)
