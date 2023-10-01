from django.db import models
# from django.conf import settings
import datetime

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
    MALE = "Male"
    FEMALE = "Female" 
           
    TYPE_OF_GENDER_CHOICES = [
    (MALE, "Male"),
    (FEMALE,"Female"),
    ]
    
    _1A = "1A"
    _1B = "1B"
    _2A = "2A"
    _2B = "2B"
    _3A = "3A"
    _3B = "3B"
    NONE_YET = "NONE YET"
    CLASSROOM_FOR_FORM_TEACHER_CHOICES = [
    (_1A, "1A"),
    (_1B, "1B"),
    (_2A, "2A"),
    (_2B, "2B"),
    (_3A, "3A"),
    (_3B, "3B"),
    (NONE_YET, "NONE YET"),
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
    form_teacher                    = models.CharField(
                                        max_length=10,
                                        choices=CLASSROOM_FOR_FORM_TEACHER_CHOICES,
                                        default=NONE_YET, 
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
    relationship_status             = models.CharField(max_length=10, blank=False, null=False, default='')
    
        
    def __str__(self):
        return self.othernames + ' ' + self.surname
    
    @property
    def age_now(self):
        today = datetime.datetime.now()
        year_today = today.year
        year_birth = self.date_of_birth.year
        age = year_today - year_birth
        return age
    
    @property
    def rtd_period(self):
        today = datetime.datetime.now()
        year_today = today.year  
        year_birth = self.date_of_birth.year
        
        year_difference = year_today - year_birth
        
        
        # calculating the month for retirement
        year_today_month = today.month
        year_birth_month = self.date_of_birth.month
        
        if (year_difference == 60)  and (year_birth_month < year_today_month):
            month_left = year_today_month - year_birth_month
            return  "You have " + str(month_left) + " month(s) left retire."
        
        elif (year_difference == 60) and (year_today_month == year_birth_month):
            return "Retires in this month"
        
        elif (year_difference == 60) and (year_birth_month > year_today_month):
            month_left = year_birth_month - year_today_month
            return  "Retired " + str(month_left) + " month(s) ago."
        
        elif year_difference > 60:
            return "Long Retired " + str(year_difference - 60) + " years ago"
        
        else:
            return str(60 - year_difference) +" "+ "more year(s)"
        
    def save(self, *args, **kwargs):
        for field_name in ['surname', 'othernames','residence', 'subjects_teaching', 'relationship_status' ]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.title())
        super(TeacherRecord, self).save(*args, **kwargs)
    
    
class TeacherRecordAdmin(models.Model):
    MALE = "Male"
    FEMALE = "Female" 
           
    TYPE_OF_GENDER_CHOICES = [
    (MALE, "Male"),
    (FEMALE,"Female"),
    ]
    
    _1A = "1A"
    _1B = "1B"
    _2A = "2A"
    _2B = "2B"
    _3A = "3A"
    _3B = "3B"
    NONE_YET = "NONE YET"
    CLASSROOM_FOR_FORM_TEACHER_CHOICES = [
    (_1A, "1A"),
    (_1B, "1B"),
    (_2A, "2A"),
    (_2B, "2B"),
    (_3A, "3A"),
    (_3B, "3B"),
    (NONE_YET, "NONE YET"),
    ]
    user                            = models.ForeignKey(User, on_delete=models.CASCADE)
    surname                         = models.CharField(max_length=10, blank=False)
    othernames                      = models.CharField(max_length=40, blank=False)
    date_of_birth                   = models.DateField()
    email                           = models.EmailField(max_length=50, blank=False)
    staff_ID                        = models.CharField(max_length=7, blank=False)
    NTC_no                          = models.CharField(max_length=15, blank=False)
    regd_no                         = models.CharField(max_length=7, blank=False)
    SSNIT_no                        = models.CharField(max_length=13, blank=False)
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
    form_teacher                    = models.CharField(
                                        max_length=10,
                                        choices=CLASSROOM_FOR_FORM_TEACHER_CHOICES,
                                        default=NONE_YET, 
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
    relationship_status             = models.CharField(max_length=10, blank=False, null=False, default='')
        
    def __str__(self):
        return self.othernames + ' ' + self.surname
    
    @property
    def age_now(self):
        today = datetime.datetime.now()
        year_today = today.year
        year_birth = self.date_of_birth.year
        age = year_today - year_birth
        return age
    
    @property
    def rtd_period(self):
        today = datetime.datetime.now()
        year_today = today.year  
        year_birth = self.date_of_birth.year
        
        year_difference = year_today - year_birth
        
        
        # calculating the month for retirement
        year_today_month = today.month
        year_birth_month = self.date_of_birth.month
        
        if (year_difference == 60)  and (year_birth_month < year_today_month):
            month_left = year_today_month - year_birth_month
            return  "You have " + str(month_left) + " month(s) left retire."
        
        elif (year_difference == 60) and (year_today_month == year_birth_month):
            return "Retires in this month"
        
        elif (year_difference == 60) and (year_birth_month > year_today_month):
            month_left = year_birth_month - year_today_month
            return  "Retired " + str(month_left) + " month(s) ago."
        
        elif year_difference > 60:
            return "Long Retired " + str(year_difference - 60) + " years ago"
        
        else:
            return str(60 - year_difference) +" "+ "more year(s)"
    
    def save(self, *args, **kwargs):
        for field_name in ['surname', 'othernames', 'residence','subjects_teaching','relationship_status' ]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.title())
        super(TeacherRecordAdmin, self).save(*args, **kwargs)