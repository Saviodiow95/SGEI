# Generated by Django 3.1.3 on 2020-11-13 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editais', '0004_auto_20201112_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='edital',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='editais'),
        ),
    ]