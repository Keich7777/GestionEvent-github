from django.contrib import admin
from .models import Utilisateur

# Register your models here.
@admin.register(Utilisateur)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','nom','mot_de_passe')