import json

# django-import
from django.core.management.base import BaseCommand
# app-import
from activityapp.models import Member, ActivityPeriod


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            data_list = json.load(f)
            # print(data_list['members'])

        for data in data_list['members']:
            data['tz'] = data.pop('tz')
            data['name'] = data.pop('real_name')
            member = Member.objects.create(member_id=data.pop(
                'id'), realname=data['name'], username=data['name'], tz=data['tz'])
            for activity_time in data['activity_periods']:
                ActivityPeriod.objects.create(member=member, start_time=activity_time.pop(
                    'start_time'), end_time=activity_time.pop('end_time'))
