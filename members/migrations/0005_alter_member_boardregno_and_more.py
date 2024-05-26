# Generated by Django 5.0.5 on 2024-05-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_rename_fullname_member_affiliation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='BoardRegNo',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='member',
            name='DateRegistration',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='Email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='IDNumber',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='member',
            name='MemberNo',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='member',
            name='Phone',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='member',
            name='PostalCode',
            field=models.IntegerField(max_length=15),
        ),
    ]