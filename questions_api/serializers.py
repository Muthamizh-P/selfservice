from rest_framework import serializers
from questions_api.models import *


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('question', 'answer')
