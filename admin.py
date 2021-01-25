from django.contrib import admin

# Register your models here.
from .models import user_login,user_profile,job_profile,user_searches,user_searches_result,user_messages,job_master,\
    data_set,blocked_messages,user_photos,job_profile_photos

admin.site.register(user_login)
admin.site.register(user_profile)
admin.site.register(job_profile)
admin.site.register(user_searches)
admin.site.register(user_searches_result)
admin.site.register(user_messages)
admin.site.register(job_master)
admin.site.register(data_set)
admin.site.register(blocked_messages)
admin.site.register(user_photos)
admin.site.register(job_profile_photos)