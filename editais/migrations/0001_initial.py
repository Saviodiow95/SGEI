# Generated by Django 3.1.3 on 2020-11-06 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('peso', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Alternativas',
                'verbose_name_plural': 'Alternativa',
            },
        ),
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('status', models.CharField(choices=[('ab', 'Aberto'), ('em', 'Em analise'), ('fn', 'Finalizado')], default='ab', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Editais',
                'verbose_name_plural': 'Edital',
            },
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ap', 'Aprovado'), ('re', 'Reprovado'), ('an', 'Analise'), ('fn', 'Finalizda')], default='ab', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editais.edital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Incrições',
                'verbose_name_plural': 'Incrição',
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='incricoes')),
                ('resposta_aberta', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alternativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editais.alternativa')),
                ('incricao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editais.inscricao')),
            ],
            options={
                'verbose_name': 'Respostas',
                'verbose_name_plural': 'Resposta',
            },
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('is_aberta', models.BooleanField(default=False)),
                ('has_arquivo', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editais.edital')),
            ],
            options={
                'verbose_name': 'Perguntas',
                'verbose_name_plural': 'Pergunta',
            },
        ),
        migrations.AddField(
            model_name='alternativa',
            name='pergunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editais.pergunta'),
        ),
    ]
