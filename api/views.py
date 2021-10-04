from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import FilterSet, DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

from event.models import Event
from . import serializers


class EventFilter(FilterSet):
    date = DateFromToRangeFilter(field_name='date')

    class Meta:
        model = Event
        fields = ['date']


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EventFilter

    def perform_create(self, serializer):
        serializer.save()

    def delete(self, request):
        Event.objects.all().delete()
        return Response('success delete')


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer
