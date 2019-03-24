from django.db import models
import datetime

from apps.greenhouse.utils import get_unique_slug


class AutoDateModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.DateTimeField(null=True, default=False)

    def delete(self):
        self.is_deleted = datetime.datetime.now()
        self.save()

    def restore(self):
        self.is_deleted = None
        self.save()

    class Meta:
        abstract = True


class ElementSolution(models.Model):
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('authorization.CustomUser', on_delete=models.CASCADE)
    class Meta:
       unique_together = ("label", "owner")
    
    def __str__(self):
        return self.label

class Solution(models.Model):
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('authorization.CustomUser', on_delete=models.CASCADE)
    elements_solution = models.ManyToManyField(ElementSolution)
    class Meta:
       unique_together = ("label", "owner")
    
    def __str__(self):
        return self.label