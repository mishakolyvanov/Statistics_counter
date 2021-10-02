from rest_framework import generics

from event.models import Event
from . import serializers


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer

    def perform_create(self, serializer):
        serializer.save()


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer
