from django.contrib import admin
from .models import UserDetail
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.


admin.site.register(UserDetail)