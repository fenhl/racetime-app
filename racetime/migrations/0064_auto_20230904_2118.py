# Generated by Django 3.2.20 on 2023-09-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0063_auto_20230901_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='actions',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
