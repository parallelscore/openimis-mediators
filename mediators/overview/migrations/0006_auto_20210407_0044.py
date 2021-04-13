# Generated by Django 2.2 on 2021-04-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0005_configs_sosys_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='configs',
            name='mediator_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='configs',
            name='openhim_passkey',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='configs',
            name='openhim_user',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='configs',
            name='openimis_passkey',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='configs',
            name='openimis_user',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]