from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import School, TeacherRecord, TeacherRecordAdmin


class RegisterForm(UserCreationForm):
    last_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}) )
    first_name = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Othernames'}) )
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}) )
   
    class Meta:
       model = User
       fields = ('last_name','first_name', 'username', 'email', 'password1', 'password2')
       
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['municipal'].label = ''
        self.fields['year_estd'].label = ''
        self.fields['type'].label = ''
        self.fields['emis_code'].label = ''
        self.fields['head_name'].label = ''
        self.fields['email'].label = ''
        self.fields['tel_no'].label = ''
        self.fields['digital_add'].label = ''
        self.fields['location'].label = ''
        self.fields['sch_no'].label = ''

class DateInputForm(forms.DateInput):
    input_type = 'date'
        
class TeacherRecordForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInputForm)
    date_promoted_to_rank = forms.DateField(widget=DateInputForm)
    date_of_first_appointment = forms.DateField(widget=DateInputForm)
    date_posted_to_present_station = forms.DateField(widget=DateInputForm)
    date_of_academic_qualification = forms.DateField(widget=DateInputForm)
    date_of_prof_qualification = forms.DateField(widget=DateInputForm)

    class Meta:
        model = TeacherRecord
        fields = "__all__"
        
        
    def __init__(self, *args, **kwargs):
        super(TeacherRecordForm, self).__init__(*args, **kwargs)
        # self.fields['user'].widget.attrs['disabled'] = True
        # self.fields['user'].widget.attrs['disabled'] = True
        
        self.fields['user'].label = ''
        self.fields['surname'].label = ''
        self.fields['othernames'].label = ''
        
        self.fields['date_of_birth'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['email'].label = ''
        self.fields['staff_ID'].label = ''
        self.fields['NTC_no'].label = ''
        self.fields['regd_no'].label = ''
        self.fields['SSNIT_no'].label = ''
        self.fields['present_rank'].label = ''
        
        self.fields['date_promoted_to_rank'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['contact_no'].label = ''
        self.fields['residence'].label = ''
        self.fields['salary_level'].label = ''
        self.fields['periods_per_week'].label = ''
        self.fields['previous_station'].label = ''
        self.fields['gender'].label = ''
        
        self.fields['date_of_first_appointment'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['date_posted_to_present_station'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['subjects_teaching'].label = ''
        self.fields['bank_name'].label = ''
        self.fields['account_no'].label = ''
        self.fields['academic_qualification'].label = ''
        
        self.fields['date_of_academic_qualification'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['prof_qualification'].label = ''
        
        self.fields['date_of_prof_qualification'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['duties_assigned'].label = ''
        self.fields['profile_image'].label = ''
        

class TeacherRecordAdminForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInputForm)
    date_promoted_to_rank = forms.DateField(widget=DateInputForm)
    date_of_first_appointment = forms.DateField(widget=DateInputForm)
    date_posted_to_present_station = forms.DateField(widget=DateInputForm)
    date_of_academic_qualification = forms.DateField(widget=DateInputForm)
    date_of_prof_qualification = forms.DateField(widget=DateInputForm)

    class Meta:
        model = TeacherRecordAdmin
        fields = "__all__"
        
        
    def __init__(self, *args, **kwargs):
        super(TeacherRecordAdminForm, self).__init__(*args, **kwargs)
        # self.fields['user'].widget.attrs['disabled'] = True
        # self.fields['user'].widget.attrs['disabled'] = True
        
        self.fields['user'].label = ''
        self.fields['surname'].label = ''
        self.fields['othernames'].label = ''
        
        self.fields['date_of_birth'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['email'].label = ''
        self.fields['staff_ID'].label = ''
        self.fields['NTC_no'].label = ''
        self.fields['regd_no'].label = ''
        self.fields['SSNIT_no'].label = ''
        self.fields['present_rank'].label = ''
        
        self.fields['date_promoted_to_rank'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['contact_no'].label = ''
        self.fields['residence'].label = ''
        self.fields['salary_level'].label = ''
        self.fields['periods_per_week'].label = ''
        self.fields['previous_station'].label = ''
        self.fields['gender'].label = ''
        
        self.fields['date_of_first_appointment'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['date_posted_to_present_station'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['subjects_teaching'].label = ''
        self.fields['bank_name'].label = ''
        self.fields['account_no'].label = ''
        self.fields['academic_qualification'].label = ''
        
        self.fields['date_of_academic_qualification'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['prof_qualification'].label = ''
        
        self.fields['date_of_prof_qualification'].label = ''
        self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Format eg: 12-23-2023 </small></span>'
        
        self.fields['duties_assigned'].label = ''
        self.fields['profile_image'].label = ''