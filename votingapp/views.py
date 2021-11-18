from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.

class home(TemplateView):
    template_name = 'home.html'

class poll_list (ListView):
    model = Poll
    def get_queryset(self):
        return Poll.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class poll_create(LoginRequiredMixin, CreateView):
    form_class = PollForm
    model = Poll

    login_url = '/login'
    redirect_field_name = 'votingapp/poll_details.html'

class poll_update(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'votingapp/poll_details.html'

    form_class = PollForm
    model = Poll
