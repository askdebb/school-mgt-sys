from django.db import models
# from django.conf import settings
# import datetime

from django.contrib.auth.models import User
#
# Create your models here.


class School(models.Model):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"    
    TYPE_OF_SCHOOL_CHOICES = [
    (PUBLIC, "Public"),
    (PRIVATE,"Private"),   
    ]
    
    name            = models.CharField(max_length=150,blank=False)
    municipal       = models.CharField(max_length=50 ,blank=False)
    year_estd       = models.CharField(max_length=4, blank=False)
    type            = models.CharField(
                        max_length=7 ,
                        choices= TYPE_OF_SCHOOL_CHOICES,
                        default=PUBLIC,
                        blank=False)
    
    emis_code       = models.CharField(max_length=50, blank=False)
    head_name       = models.CharField(max_length=50, blank=False)
    email           = models.EmailField(max_length=50, blank=False)
    tel_no          = models.CharField(max_length=10, blank=False)
    digital_add     = models.CharField(max_length=13, blank=False)
    location        = models.CharField(max_length=20, blank=False)
    sch_no          = models.CharField(max_length=7, blank=False)
    
    
    
    
    def __str__(self):
        return self.name
    
    
class TeacherRecord(models.Model):
    MALE = "M"
    FEMALE = "F"    
    TYPE_OF_GENDER_CHOICES = [
    (MALE, "Male"),
    (FEMALE,"Female"),
    
    ]
    user                            = models.OneToOneField(User, on_delete=models.CASCADE)
    surname                         = models.CharField(max_length=10, blank=False)
    othernames                      = models.CharField(max_length=40, blank=False)
    date_of_birth                   = models.DateField()
    email                           = models.EmailField(max_length=50, blank=False)
    staff_ID                        = models.CharField(max_length=7, blank=False)
    NTC_no                          = models.CharField(max_length=15, blank=False)
    regd_no                         = models.CharField(max_length=7, blank=False)
    SSNIT_no                        = models.CharField(max_length=15, blank=False)
    present_rank                    = models.CharField(max_length=40, blank=False)
    date_promoted_to_rank           = models.DateField()
    contact_no                      = models.CharField(max_length=10, blank=False)
    residence                       = models.CharField(max_length=40, blank=False)
    salary_level                    = models.CharField(max_length=10, blank=False)
    periods_per_week                = models.IntegerField( blank=False)
    previous_station                = models.CharField(max_length=40, blank=False)
    gender                          = models.CharField(
                                        max_length=7,
                                        choices=TYPE_OF_GENDER_CHOICES,
                                        default=MALE, 
                                        blank=False)
    date_of_first_appointment       = models.DateField()
    date_posted_to_present_station  = models.DateField()
    subjects_teaching               = models.CharField(max_length=50, blank=False)
    bank_name                       = models.CharField(max_length=40, blank=False)
    account_no                      = models.CharField(max_length=20, blank=False)
    academic_qualification          = models.CharField(max_length=60, blank=False)
    date_of_academic_qualification  = models.DateField()
    prof_qualification              = models.CharField(max_length=60, blank=False)
    date_of_prof_qualification      = models.DateField()
    duties_assigned                 = models.CharField(max_length=60, blank=False)
    profile_image                   = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=100)
    
        
    def __str__(self):
        return self.othernames + ' ' + self.surname
    
    
class TeacherRecordAdmin(models.Model):
    MALE = "M"
    FEMALE = "F"    
    TYPE_OF_GENDER_CHOICES = [
    (MALE, "Male"),
    (FEMALE,"Female"),
    
    ]
    user                            = models.ForeignKey(User, on_delete=models.CASCADE)
    surname                         = models.CharField(max_length=10, blank=False)
    othernames                      = models.CharField(max_length=40, blank=False)
    date_of_birth                   = models.DateField()
    email                           = models.EmailField(max_length=50, blank=False)
    staff_ID                        = models.CharField(max_length=7, blank=False)
    NTC_no                          = models.CharField(max_length=15, blank=False)
    regd_no                         = models.CharField(max_length=7, blank=False)
    SSNIT_no                        = models.CharField(max_length=15, blank=False)
    present_rank                    = models.CharField(max_length=40, blank=False)
    date_promoted_to_rank           = models.DateField()
    contact_no                      = models.CharField(max_length=10, blank=False)
    residence                       = models.CharField(max_length=40, blank=False)
    salary_level                    = models.CharField(max_length=10, blank=False)
    periods_per_week                = models.IntegerField( blank=False)
    previous_station                = models.CharField(max_length=40, blank=False)
    gender                          = models.CharField(
                                        max_length=7,
                                        choices=TYPE_OF_GENDER_CHOICES,
                                        default=MALE, 
                                        blank=False)
    date_of_first_appointment       = models.DateField()
    date_posted_to_present_station  = models.DateField()
    subjects_teaching               = models.CharField(max_length=50, blank=False)
    bank_name                       = models.CharField(max_length=40, blank=False)
    account_no                      = models.CharField(max_length=20, blank=False)
    academic_qualification          = models.CharField(max_length=60, blank=False)
    date_of_academic_qualification  = models.DateField()
    prof_qualification              = models.CharField(max_length=60, blank=False)
    date_of_prof_qualification      = models.DateField()
    duties_assigned                 = models.CharField(max_length=60, blank=False)
    profile_image                   = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=100)
    
        
    def __str__(self):
        return self.othernames + ' ' + self.surname
    
        