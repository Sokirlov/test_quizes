from rest_framework import serializers
from .models import QuizeName, Questions, SingelAnswer, Client


class SingelAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingelAnswer
        fields = ['answer']

class QuestionsSerializer(serializers.ModelSerializer):
    answerVariant = SingelAnswerSerializer(many=True)
    class Meta:
        model = Questions
        fields = ['question', 'questionType', 'answerVariant', ]

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class QuizeNameSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionsSerializer(many=True)
    class Meta:
        model = QuizeName
        fields = ['name', 'dataStart', 'dateFinish', 'description', 'status', 'questions']
