# Generated by Django 2.2.5 on 2019-10-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20191010_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='city',
            new_name='county',
        ),
        migrations.AddField(
            model_name='company',
            name='company_logo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
