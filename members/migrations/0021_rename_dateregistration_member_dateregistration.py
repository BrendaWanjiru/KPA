# Generated by Django 5.0.5 on 2024-05-17 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0020_rename_memberno_member_memberid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='DateRegistration',
            new_name='Dateregistration',
        ),
    ]
