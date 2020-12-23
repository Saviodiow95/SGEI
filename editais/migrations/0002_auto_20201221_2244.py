# Generated by Django 3.1.3 on 2020-12-22 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao',
            name='nivel_vul',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='status',
            field=models.CharField(choices=[('ap', 'Aprovado'), ('re', 'Reprovado'), ('an', 'Em Analise')], default='an', max_length=2),
        ),
    ]