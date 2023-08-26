from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # school system general links
    path ('', views.home, name='home'),
    path ('sch_query_unsigned/', views.unsignedSearch, name='sch_query_unsigned'),
    path ('home_search/', views.homeSearch, name='home-search'),
    
    
    # school records mgt  links
    path ('teacher-record-form/', views.teacherRecordForm, name='teacher-record-form'),
    path ('teacher-profile/', views.teacherProfile, name='teacher-profile'),
    path ('teacher-list/<int:pk>', views.teacherList, name='teacher-list'),
    
    
    # school account mgt links
    path ('login/', views.signIn, name='sign-in'),
    path ('signed-out/', views.signOut, name='signed-out'),
    path ('register/', views.register, name='register'),
    path ('register-school/', views.registerSchool, name='register-school'),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
