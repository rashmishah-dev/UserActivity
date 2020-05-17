from django.shortcuts import render

from rest_framework import viewsets

from .models import Member, ActivityPeriod
from .serializers import MemberSerializer, ActivityPeriodSerializer

# Create your views here.


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
