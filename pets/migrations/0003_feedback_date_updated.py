# Generated by Django 4.2.1 on 2024-04-10 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]