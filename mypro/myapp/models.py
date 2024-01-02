from django.db import models

# Create your models here.
class whole_city(models.Model):
    city_names=models.TextField(max_length=60)

    def __str__(self):
        return self.city_names