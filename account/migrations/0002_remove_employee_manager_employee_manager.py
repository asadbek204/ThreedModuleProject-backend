# Generated by Django 5.0 on 2024-01-08 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='manager',
        ),
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employees', to='account.employee', verbose_name='manager'),
        ),
    ]
