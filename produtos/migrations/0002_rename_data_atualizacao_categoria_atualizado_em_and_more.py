# Generated by Django 4.2 on 2024-06-26 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='data_atualizacao',
            new_name='atualizado_em',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='data_criacao',
            new_name='criado_em',
        ),
        migrations.RenameField(
            model_name='embalagem',
            old_name='data_atualizacao',
            new_name='atualizado_em',
        ),
        migrations.RenameField(
            model_name='embalagem',
            old_name='data_criacao',
            new_name='criado_em',
        ),
        migrations.RenameField(
            model_name='fornecedor',
            old_name='data_atualizacao',
            new_name='atualizado_em',
        ),
        migrations.RenameField(
            model_name='fornecedor',
            old_name='data_criacao',
            new_name='criado_em',
        ),
        migrations.RenameField(
            model_name='local',
            old_name='data_atualizacao',
            new_name='atualizado_em',
        ),
        migrations.RenameField(
            model_name='local',
            old_name='data_criacao',
            new_name='criado_em',
        ),
        migrations.RenameField(
            model_name='movimentacao',
            old_name='data_atualizacao',
            new_name='atualizado_em',
        ),
        migrations.RenameField(
            model_name='movimentacao',
            old_name='data_criacao',
            new_name='criado_em',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='data_atualizacao',
            new_name='atualizado_em',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='data_criacao',
            new_name='criado_em',
        ),
    ]
