# Generated by Django 3.1.3 on 2020-12-22 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editais', '0002_auto_20201221_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='status',
            field=models.CharField(choices=[('df', 'Defirido'), ('in', 'Indefirido'), ('an', 'Em Analise')], default='an', max_length=2),
        ),
    ]
