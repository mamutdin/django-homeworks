# Generated by Django 4.1 on 2022-08-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_tag_name_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(through='articles.ArticleTag', to='articles.article'),
        ),
    ]
