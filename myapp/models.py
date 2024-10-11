from django.db import models #type:ignore
class student(models.Model):
    name=models.CharField(max_length=20,null=True)
    username=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=20,null=True)
    phonemnumber=models.CharField(max_length=20,null=True)
    place=models.CharField(max_length=20,null=True)
def __str__(self):
    return self.name+','+self.username+','+self.password+','+self.phonenumber+','+self.place




