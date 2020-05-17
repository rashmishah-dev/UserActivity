from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    member_id = models.CharField(max_length=30, unique=True, verbose_name="id")
    realname = models.CharField(max_length=30)
    tz = models.CharField(max_length=30)

    @property
    def activity_periods(self):
        return self.member_activity.all()


class ActivityPeriod(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="member_activity")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return '%s: %s' % (self.start_time, self.end_time)
