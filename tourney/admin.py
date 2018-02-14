from django.contrib import admin

from .models import Profile,Tourney,Match

admin.site.register(Profile)
admin.site.register(Tourney)
admin.site.register(Match)
