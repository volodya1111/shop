# Generated by Django 3.2.5 on 2021-07-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_remove_watch_memory'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='description',
            field=models.TextField(blank=True, max_length=4096, null=True),
        ),
    ]