from django.db import models

# Create your models here.


class School(models.Model):
    name            = models.CharField(max_length=150,blank=False)
    municipal       = models.CharField(max_length=50 ,blank=False)
    year_estd       = models.CharField(max_length=4, blank=False)
    type            = models.CharField(max_length=7 , blank=False)
    emis_code       = models.IntegerField(blank=False)
    head_name       = models.CharField(max_length=50, blank=False)
    email           = models.EmailField(max_length=50, blank=False)
    tel_no          = models.CharField(max_length=10, blank=False)
    digital_add     = models.CharField(max_length=13, blank=False)
    location        = models.CharField(max_length=20, blank=False)
    sch_no          = models.CharField(max_length=7, blank=False)
    
    
    def __str__(self):
        return self.name