from django.contrib import admin
from .models import Profile, UserInstrument, UserGenere, UserCooperation, UserKindOfProfile

admin.site.register(Profile)
admin.site.register(UserInstrument)
admin.site.register(UserGenere)
admin.site.register(UserCooperation)
admin.site.register(UserKindOfProfile)