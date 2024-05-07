from django.db import models

class mode1(models.Model):
    name=models.CharField(max_length=40)
    gmail=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    
    class Meta:
        db_table="user_data"