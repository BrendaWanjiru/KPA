from django.contrib import admin
from .models import Member


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("MemberID", "Fullname", "Email", "Phone", "IDNumber", "BoardRegNo", "Designation", "SubSpecialization", "Workstation", "Affiliation", "PostalAddress", "PostalCode", "TownorCity", "DateRegistration", "BackupEmail", "Approved", "Status", "Roles",)
  list_display_links = ("MemberID", "Fullname", "Email", "Phone", "IDNumber", "BoardRegNo", "Designation", "SubSpecialization", "Workstation", "Affiliation", "PostalAddress", "PostalCode", "TownorCity", "DateRegistration", "BackupEmail", "Approved", "Status", "Roles",)

admin.site.register(Member, MemberAdmin)
