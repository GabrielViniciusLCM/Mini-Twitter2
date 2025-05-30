# Generated by Django 5.1.1 on 2025-05-01 15:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='autor',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='conteudo',
            field=models.TextField(default='Texto padrão', max_length=280),
        ),
        migrations.AddField(
            model_name='post',
            name='criado_em',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
