from django.db import models

# Create your models here.
class Items1(models.Model):
    item_name1=models.CharField(max_length=122)
    item_desc1=models.CharField(max_length=122)
    item_price1=models.IntegerField()
    item_image=models.CharField(max_length=5000,default='https://t3.ftcdn.net/jpg/07/10/34/00/240_F_710340033_NThiSbQxwd2tK9mzDDFB68OTkfKPhdC5.jpg')