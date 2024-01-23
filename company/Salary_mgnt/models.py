from django.db import models

# Create your models here.
class salary(models.Model):
    Name=models.CharField(max_length=50) 
    Sal_23=models.IntegerField() 
    Sal_24=models.IntegerField() 
    
    def __str__(self):
        return str(
            (
                self.Name
            )
        )

# path(sal/<int:sal>/) > views(sal) > templates


# button1     sal/1/
# button2     sal/2/
    