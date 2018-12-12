from django.db import models
class product(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    Name=models.CharField(max_length=20)
    Description=models.TextField(blank=True,default='')
    price=models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return self.Name

