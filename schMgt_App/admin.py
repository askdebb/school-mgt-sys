from django.contrib import admin
from  .models  import School, TeacherRecord, TeacherRecordAdmin

# Register your models here.
admin.site.register(School)
admin.site.register(TeacherRecord)
admin.site.register(TeacherRecordAdmin)

