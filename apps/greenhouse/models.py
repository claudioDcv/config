from django.db import models

from .utils import get_unique_slug

class AutoDateModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Plant(AutoDateModel):
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

    description = models.TextField()

    temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)