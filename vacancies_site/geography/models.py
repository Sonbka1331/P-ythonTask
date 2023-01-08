from django.db import models


class Geography(models.Model):

    name = models.CharField(max_length=300)
    data = models.CharField(max_length=1000)
    cities = models.CharField(max_length=1000)
    individual_id = models.CharField(max_length=300)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def data_as_dict(self):
        values = {}
        data = self.data.split(', ')
        cities = self.cities.split(', ')
        for i in data:
            index = data.index(i)
            values[cities[index]] = i
        return values
