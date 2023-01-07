from django.db import models


class DemandData(models.Model):

    name = models.CharField(max_length=300)
    data = models.CharField(max_length=500)
    individual_id = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
