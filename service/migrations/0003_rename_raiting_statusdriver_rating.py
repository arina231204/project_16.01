# Generated by Django 4.1.5 on 2023-01-16 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_remove_statusdriver_point_statusdriver_raiting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusdriver',
            old_name='raiting',
            new_name='rating',
        ),
    ]