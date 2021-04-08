"""
Models for polls, poll questions and an associative table PollsUsers,
that is used to store information on which user took which poll and record
users' answers.
"""
from uuid import uuid4

from django.conf import settings
from django.db import models


class Poll(models.Model):
    """
    Model for a poll. Apart from obvious fields like the name of the poll
    or UUID, it also stores start and finish dates, detailed description
    and the 'is_active' flag.
    """
    uuid = models.UUIDField(primary_key=True,
                            default=uuid4,
                            verbose_name='id')
    name = models.CharField(max_length=64, verbose_name='name')
    start_date = models.DateTimeField(null=False,
                                      verbose_name='start datetime')
    finish_date = models.DateTimeField(null=False,
                                       verbose_name='finish datetime')
    description = models.CharField(max_length=256,
                                   blank=True,
                                   verbose_name='detailed description')
    is_active = models.BooleanField(default=True, verbose_name='is active?')

    def __str__(self):
        return "%s - %s" % (self.name, self.description)


class PollQuestion(models.Model):
    """
    Model for a poll question. It has a Many-to-One relationship field that
    connects it with the Poll table (one poll can have multiple questions).
    Also stores question type and text.
    """
    TEXT = 'TXT'
    MULTIPLE_CHOICE = 'MULT'
    SINGLE_CHOICE = 'SING'
    QUESTION_TYPES = [
        (TEXT, 'text answer'),
        (MULTIPLE_CHOICE, 'multiple choice'),
        (SINGLE_CHOICE, 'single choice')
    ]

    uuid = models.UUIDField(primary_key=True,
                            default=uuid4,
                            verbose_name='id')
    poll = models.ForeignKey(Poll,
                             related_name='questions',
                             on_delete=models.CASCADE,
                             verbose_name='poll id')
    question_text = models.CharField(max_length=256,
                                     blank=False,
                                     verbose_name="question's text")
    question_type = models.CharField(max_length=4,
                                     choices=QUESTION_TYPES,
                                     default=TEXT,
                                     verbose_name='type of question')

    def __str__(self):
        return "%s (%s)" % (self.question_text, self.question_type)


class PollsUsers(models.Model):
    """
    An associative, cross-reference table to keep track of what polls
    has a user taken, and which answers he gave to the questions.
    """
    uuid = models.UUIDField(primary_key=True,
                            default=uuid4,
                            verbose_name='id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='users_polls',
                             on_delete=models.DO_NOTHING,
                             verbose_name="user's id")
    poll = models.ForeignKey(Poll,
                             related_name='answered_polls',
                             on_delete=models.DO_NOTHING,
                             verbose_name="poll's id")
    poll_question = models.ForeignKey(PollQuestion,
                                      related_name='answered_questions',
                                      on_delete=models.DO_NOTHING,
                                      verbose_name="question's id")
    user_answer = models.CharField(max_length=512,
                                   blank=True,
                                   verbose_name="user's answer")
