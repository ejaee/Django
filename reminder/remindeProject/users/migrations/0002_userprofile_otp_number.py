# Generated by Django 5.0 on 2024-01-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='otp_number',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
