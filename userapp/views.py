"""
Class-based views for the API.
"""
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from pollapp.models import Poll, PollsUsers, PollQuestion
from pollapp.serializers import PollModelSerializer, \
    PollsUsersModelSerializer, PollQuestionModelSerializer


class ActivePollsView(ListAPIView):
    """
    This view returns the list of all the polls active at the moment.
    """
    queryset = Poll.objects.filter(is_active=True)
    serializer_class = PollModelSerializer


class TakePollView(CreateAPIView):
    """
    This view accepts POST-data for answered questions. It accepts the
    data question by question, creating entries to the PollsUsers table,
    where each row - is a combination of user, poll question and user's
    answer to that question. This is a POST-only view, GET-requests are
    not accepted.
    """
    queryset = PollsUsers.objects.all()
    serializer_class = PollsUsersModelSerializer


class UsersCompletedPollsView(ListAPIView):
    """
    This view returns a list of all the questions (their UUIDs to be precise)
    answered by a certain user. The returned data also includes the UUIDs of
    the polls, and the user's UUID.
    """
    serializer_class = PollsUsersModelSerializer

    def get_queryset(self):
        """
        Overrides the method from the parent class. Extracts the user's
        UUID from the request's kwargs and returns the queryset of this user's
        answers to questions.
        """
        uuid = self.kwargs.get('pk')
        return PollsUsers.objects.filter(user=uuid)


class AdminPollViewSet(ModelViewSet):
    """
    ViewSet used to do CRUD actions over the Poll table. The caveat
    being that it only allows modifying/updating/deleting objects
    to users with admin privileges ('is_staff' = True).
    """
    queryset = Poll.objects.all()
    serializer_class = PollModelSerializer
    permission_classes = [permissions.IsAdminUser]


class AdminPollQuestionViewSet(ModelViewSet):
    """
    ViewSet used to do CRUD actions over the PollQuestion table. The caveat
    being that it only allows modifying/updating/deleting objects
    to users with admin privileges ('is_staff' = True).
    """
    queryset = PollQuestion.objects.all()
    serializer_class = PollQuestionModelSerializer
    permission_classes = [permissions.IsAdminUser]
