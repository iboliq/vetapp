from django.contrib import admin

from .models import PetModel, PetOwnerModel
# Register your models here.

class PetModelAdminTabularInline(admin.TabularInline):
    model = PetModel
    extra = 0

@admin.register(PetOwnerModel)
class PetOwnerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', "howManyPets"]
    search_fields = ['name']
    inlines = [PetModelAdminTabularInline]



@admin.register(PetModel)
class PetModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'genre', 'genus', 'age']
    search_fields = ['name', 'owner__name']