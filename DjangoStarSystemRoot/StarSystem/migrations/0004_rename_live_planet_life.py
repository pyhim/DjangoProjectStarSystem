# Generated by Django 3.2.5 on 2021-07-25 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StarSystem', '0003_auto_20210725_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planet',
            old_name='live',
            new_name='life',
        ),
    ]
