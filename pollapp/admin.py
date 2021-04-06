from django.contrib import admin

from .models import Poll, PollQuestion, PollsUsers

admin.site.register((Poll, PollQuestion, PollsUsers))
