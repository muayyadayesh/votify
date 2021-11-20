from django.contrib import admin
from votingapp.models import *

# Registering Poll & Answer models inside the admin section .
admin.site.register(Poll)
admin.site.register(Answer)
