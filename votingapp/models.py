from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Poll(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256, unique=True)
    created_date = models.DateTimeField(default=timezone.now())
    last_update = models.DateTimeField(default=timezone.now())

    def set_last_update(self):
        self.last_update = timezone.now()
        self.save()

    #Return chart data for the result page
    def get_graph_data(self):
        labels = []
        data = []
        queryset = self.options.all()

        for answer in queryset:
            labels.append(answer.title)
            data.append(answer.votes)

        return {'labels': labels, 'data': data}
    #reverse after actions
    def get_absolute_url(self):
        return reverse("votingapp:poll_details", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

#Answer object which has Answer-Poll (many-1) relationship
class Answer(models.Model):
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    isRequired = models.BooleanField()
    votes = models.IntegerField(default=0, blank=True)

    def Increase_vote(self):
        #increase the current vote count by 1
        self.votes += 1
        #update the poll recent interactions time
        self.poll.set_last_update()
        self.save()

    def get_absolute_url(self):
        return reverse("votingapp:poll_list")

    def __str__(self):
        return self.title
