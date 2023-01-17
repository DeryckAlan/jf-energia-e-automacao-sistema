# Generated by Django 4.1.5 on 2023-01-17 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Projeto', '0003_painel'),
        ('QrCode', '0004_remove_qrcode_painel_remove_qrcode_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='painel_nome',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Projeto.painel'),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='projeto_nome',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Projeto.projeto'),
        ),
    ]