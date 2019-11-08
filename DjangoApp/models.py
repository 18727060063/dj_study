from django.db import models

# Create your models here.
class NormalPeople(models.Model):
    id = models.AutoField(max_length=5,primary_key=True)
    pTel = models.CharField(max_length=11, default=" ")
    pDesc = models.CharField(max_length=20, default=" ")
    pHostName = models.CharField(max_length=8, default=" ")
    pAddress = models.IntegerField(default=0)
    pRelation = models.CharField(max_length=10, default=" ")
    pFamilyNo = models.CharField(max_length=20, default=" ")
    pSpecial = models.CharField(max_length=20, default=" ")
    pName = models.CharField(max_length=5, default=" ")
    pIdNo = models.CharField(max_length=22, default=" ")
    pGender = models.CharField(max_length=2, default=" ")
