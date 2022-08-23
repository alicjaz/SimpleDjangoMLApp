from django.db import models


class PredResults(models.Model):

    duration = models.FloatField()
    waiting = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification
