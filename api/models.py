from django.db import models

# Create your models here.
class Laptop(models.Model):
    brand=models.TextField(max_length=100,null=True)
    image=models.FileField(blank=False, null=True)
    processor=models.TextField(max_length=100,null=True)
    display=models.TextField(max_length=100,null=True)
    memory_ram=models.TextField(max_length=100,null=True)
    memory_hdd=models.TextField(max_length=50,null=True)
    price=models.TextField(max_length=100,null=True)
    def __str__(self):
        return self.id