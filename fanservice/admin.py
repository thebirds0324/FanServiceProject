from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import OfficialPost, Member, NormalPost

admin.site.register(OfficialPost)
admin.site.register(Member)
admin.site.register(NormalPost)