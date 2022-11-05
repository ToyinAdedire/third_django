from django.contrib import admin
from .models import Artiste, song, Lyric

# Register your models here.

admin.site.register(Artiste)
admin.site.register(song)
admin.site.register(Lyric)

