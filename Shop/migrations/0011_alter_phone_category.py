# Generated by Django 3.2.5 on 2021-08-02 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_auto_20210724_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='category',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.category'),
        ),
    ]
