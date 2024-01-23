from django.db import models
from Employee_mgnt.models import employee
from django.http import HttpResponseBadRequest

# Create your models here.
class dept(models.Model):
    Dep_name=models.CharField(max_length=50) 
    Floor=models.CharField(max_length=50) 
    
    def __str__(self):
        return str(
            (
                self.Dep_name,
                self.Floor
            )
        )


class Hierarchy(models.Model):
    department = models.ForeignKey(dept, on_delete=models.CASCADE, default=1)
    manager = models.ForeignKey(employee, on_delete=models.CASCADE, default=1, related_name='manager')
    teamleader = models.ForeignKey(employee, on_delete=models.CASCADE, default=1, related_name='teamleader')
    employee = models.ForeignKey(employee, on_delete=models.CASCADE, default=1, related_name='employee')

    def __str__(self):
        return str(
            (
                self.department,
                self.manager,
                self.teamleader,
                self.employee
            )
        )
