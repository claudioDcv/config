from django.db import models

from .utils import get_unique_slug

class AutoDateModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class PlantType(models.Model):
    label = models.CharField(max_length=255)
    sub_type = models.CharField(max_length=255)
    owner = models.ForeignKey('authorization.CustomUser', on_delete=models.CASCADE)

    class Meta:
       unique_together = ("label", "owner", "sub_type")
    
    def __str__(self):
        return self.sub_type + ' ' + self.label


class Group(AutoDateModel):
    label = models.CharField(max_length=255)
    owner = models.ForeignKey('authorization.CustomUser', on_delete=models.CASCADE)

    class Meta:
       unique_together = ("label", "owner")
    
    def __str__(self):
        return self.label


class Plant(AutoDateModel):
    group = models.ForeignKey('greenhouse.Group', on_delete=models.CASCADE)
    plant_type = models.ForeignKey('greenhouse.PlantType', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    birthdate = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey('authorization.CustomUser', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True)
 
    def save(self, *args, **kwargs):
        self.slug = get_unique_slug(self, 'code', 'slug')
        super().save(*args, **kwargs)  
    def __str__(self):
        return self.code

    class Meta:
       unique_together = ("owner", "slug")


class Control(AutoDateModel):
    plant = models.ForeignKey('greenhouse.Plant', on_delete=models.CASCADE)
    capture_date = models.DateTimeField(blank=True, null=True)

    temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    
    description = models.TextField(blank=True, null=True)