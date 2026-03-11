from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    def __str__(self):
        return self.name


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/')
    def __str__(self):
        return self.full_name


class Service(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField(verbose_name="Servis haqqinda malumat.")
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class (misali: bi-heart-pulse)")
    objects = models.Manager()
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
    def __str__(self):
        return self.title