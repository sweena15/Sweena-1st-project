from django.db import models

# Create your models here.
class employee(models.Model):
    Name=models.CharField(max_length=50) 
    Designation=models.CharField(max_length=50) 
    Email=models.CharField(max_length=50) 
    Dep_name=models.CharField(max_length=50) 
    Manager_name=models.CharField(max_length=50)

    def __str__(self):
        return str(
            (
                self.Name,
                self.Designation
            )
        )
