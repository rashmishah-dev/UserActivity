from rest_framework import serializers
from .models import Member, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%B %d %Y %H:%M')
    end_time = serializers.DateTimeField(format='%B %d %Y %H:%M')

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')
        depth = 1


class MemberSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = Member
        fields = ('member_id', 'realname', 'tz', 'activity_periods')
