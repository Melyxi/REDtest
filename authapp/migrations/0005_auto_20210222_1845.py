# Generated by Django 3.1.7 on 2021-02-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210222_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('ADMIN', 'Administrator'), ('USER', 'User')], default='USER', max_length=50, null=True),
        ),
    ]
