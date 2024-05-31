from django.contrib import admin
from .models import Member
from django.contrib import admin
from .models import Image
from django.utils.html import format_html

class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = [ 'image_tag',]

admin.site.register(Image, ImageAdmin)

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("MemberID", "Fullname", "Email", "Phone", "IDNumber", "BoardRegNo", "Designation", "SubSpecialization", "Workstation", "Affiliation", "PostalAddress", "PostalCode", "TownorCity", "DateRegistration", "BackupEmail", "Approved", "Status", "Roles",)
  list_display_links = ("MemberID", "Fullname", "Email", "Phone", "IDNumber", "BoardRegNo", "Designation", "SubSpecialization", "Workstation", "Affiliation", "PostalAddress", "PostalCode", "TownorCity", "DateRegistration", "BackupEmail", "Approved", "Status", "Roles",)

admin.site.register(Member, MemberAdmin)
