# Generated by Django 2.2 on 2021-04-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0004_remove_configs_mediator_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='configs',
            name='sosys_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]