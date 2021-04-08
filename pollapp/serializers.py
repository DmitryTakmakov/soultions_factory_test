"""
Serializers for the polls application.
"""
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Poll, PollQuestion, PollsUsers


class PollModelSerializer(ModelSerializer):
    """
    ModelSerializer subclass for serialization of the Poll model.
    """

    class Meta:
        model = Poll
        fields = ['name',
                  'start_date', 'finish_date', 'description', 'is_active']

    def update(self, instance, validated_data):
        """
        Checks if the 'start_date' field is being updated and raises an
        exception if it is. Otherwise - a standard update method from the
        parent class.
        """
        if 'start_date' in validated_data:
            raise ValidationError(
                {'start_date': 'Данное поле обновлять нельзя!'})

        return super().update(instance, validated_data)


class PollQuestionModelSerializer(ModelSerializer):
    """
    ModelSerializer subclass for serialization of PollQuestion model.
    """
    poll = serializers.StringRelatedField()

    class Meta:
        model = PollQuestion
        fields = ['poll', 'question_text', 'question_type']


class PollsUsersModelSerializer(ModelSerializer):
    """
    ModelSerializer subclass for serialization of PollsUsers model.
    """
    user = serializers.StringRelatedField()
    poll = serializers.StringRelatedField()
    poll_question = serializers.StringRelatedField()

    class Meta:
        model = PollsUsers
        fields = ['user', 'poll', 'poll_question', 'user_answer']
