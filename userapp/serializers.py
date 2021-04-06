"""
Serializers for the user application.
"""
from rest_framework.serializers import ModelSerializer

from .models import PollUser


class PollUserModelSerializer(ModelSerializer):
    """
    Concrete implementation of the ModelSerializer class from DRF. Used
    to serialize the User model.
    """

    class Meta:
        model = PollUser
        fields = '__all__'
