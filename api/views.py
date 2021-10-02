from rest_framework import generics
from rest_framework.response import Response

from event.models import Event
from . import serializers


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer

    def perform_create(self, serializer):
        serializer.save()

    def delete(self, request):
        Event.objects.all().delete()
        return Response('success delete')


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer
