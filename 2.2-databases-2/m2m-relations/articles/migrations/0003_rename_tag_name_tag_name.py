# Generated by Django 4.1 on 2022-08-10 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_articletag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='name',
        ),
    ]
