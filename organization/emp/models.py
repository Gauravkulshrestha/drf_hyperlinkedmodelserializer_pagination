from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=120)
    emp_id = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name