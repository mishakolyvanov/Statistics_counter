from rest_framework import serializers
from event.models import Event


class EventSerializer(serializers.ModelSerializer):
    cpc = serializers.SerializerMethodField('cpc_count')
    cpm = serializers.SerializerMethodField('cpm_count')

    def cpc_count(self, event):
        return event.cost / event.clicks

    def cpm_count(self, event):
        cpm = event.cost / event.views * 1000
        return float('{:.2f}'.format(cpm))

    class Meta:
        model = Event
        fields = ['date', 'views', 'clicks', 'cost', 'cpc', 'cpm']
