# Generated by Django 4.2.5 on 2023-10-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_email_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.TextField(blank=True, null=True, verbose_name='Токен'),
        ),
    ]
