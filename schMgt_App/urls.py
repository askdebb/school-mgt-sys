from django.urls import path
from .views import home, signIn, register, registerSchool, teacherRecordForm, teacherProfile, teacherList, signOut, unsignedSearch, homeSearch

urlpatterns = [
    # school system general links
    path ('', home, name='home'),
    path ('sch_query_unsigned/', unsignedSearch, name='sch_query_unsigned'),
    path ('home_search/', homeSearch, name='home-search'),
    
    
    # school records mgt  links
    path ('teacher-record-form/', teacherRecordForm, name='teacher-record-form'),
    path ('teacher-profile/', teacherProfile, name='teacher-profile'),
    path ('teacher-list/', teacherList, name='teacher-list'),
    
    
    # school account mgt links
    path ('login/', signIn, name='sign-in'),
    path ('signed-out/', signOut, name='signed-out'),
    path ('register/', register, name='register'),
    path ('register-school/', registerSchool, name='register-school'),
]
