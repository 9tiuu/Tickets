from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tech(models.Model):
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="techs")

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

class Ticket(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    tech = models.ForeignKey(Tech, null=True, blank=True, on_delete=models.RESTRICT) 

    def __str__(self) -> str:
        return self.title # Mostrara el nombre del ticket

