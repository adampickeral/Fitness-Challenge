from django.db import models

class WorkoutEntry(models.Model):
    name = models.CharField("employee name", max_length=200)
    date = models.DateField("workout date")
