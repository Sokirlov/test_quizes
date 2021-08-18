from rest_framework import viewsets
from rest_framework import permissions
from .serializers import QuizeNameSerializer, ClientSerializer
from .models import QuizeName, Client


class QuizeNameViewSet(viewsets.ModelViewSet):
    queryset = QuizeName.objects.all().order_by('dataStart')
    serializer_class = QuizeNameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClientAllAnswersViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['post']


