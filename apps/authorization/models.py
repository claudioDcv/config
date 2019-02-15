from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  USER = 1
  HARVESTER = 2
  SUPERVISOR = 3
  ADMIN = 4
  ROLE_CHOICES = (
      (USER, 'user'),
      (HARVESTER, 'harvester'),
      (SUPERVISOR, 'supervisor'),
      (ADMIN, 'administrator'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()


class CustomUser(AbstractUser):
  roles = models.ManyToManyField(Role)

  def __str__(self):
        return self.email