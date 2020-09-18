from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=100, blank=False, default='')


class UserNotes(models.Model):
    userId = models.IntegerField()
    notes = models.TextField()
