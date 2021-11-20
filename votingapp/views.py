from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
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
class poll_new(LoginRequiredMixin, CreateView):
    form_class = PollForm
    model = Poll

    login_url = '/accounts/login'
    # redirect_field_name = '/'

@login_required
def newpoll(request):
    form = PollForm()
    if request.method == 'POST' and request.user.is_authenticated:
        #Fetch the POST data
        form = PollForm(data=request.POST)

        # print(request.POST)
        if form.is_valid():
            print('received!')
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()

            option1 = Answer(poll=obj, title=request.POST.get('option1', ''), isRequired=True)
            option2 = Answer(poll=obj, title=request.POST.get('option2', ''), isRequired=True)
            #Save mandatory answers
            option1.save()
            option2.save()

            #Save answer 3 if exists
            if request.POST.get('option3', ''):
                option3 = Answer(poll=obj, title=request.POST.get('option3', ''), isRequired=True)
                option3.save()

            #Save answer 4 if exists
            if request.POST.get('option4', ''):
                option4 = Answer(poll=obj, title=request.POST.get('option4', ''), isRequired=True)
                option4.save()
            return redirect("votingapp:poll_list")

    return render(request, 'votingapp/poll_form.html', {'form': form})

#Update the poll: LoginRequired
class poll_update(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'votingapp/poll_details.html'

    form_class = PollForm
    model = Poll

#Delete poll using deleteview: LoginRequired
class poll_delete(LoginRequiredMixin, DeleteView):
    model = Poll
    success_url = reverse_lazy('votingapp:poll_list')

#Poll result, appears after voting action
class poll_result(DetailView):
    model = Poll
    template_name = 'votingapp/poll_result.html'


class poll_vote(DetailView):
    model = Poll
    template_name = 'poll_vote.html'


#No auth required here
def poll_vote_action(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    answer.Increase_vote()
    return redirect('votingapp:poll_result', pk=answer.poll.pk)
