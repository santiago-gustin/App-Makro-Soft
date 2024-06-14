from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=50)
    work_weight_accumulated = models.IntegerField(default=0)

class Support(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.IntegerField()
    work_weight = models.IntegerField()
    assigned_to = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True, blank=True)