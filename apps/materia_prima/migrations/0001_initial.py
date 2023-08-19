# Generated by Django 4.0 on 2023-08-13 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf_cnpj', models.CharField(blank=True, max_length=14, verbose_name='CPF/CNPJ')),
                ('razao_social', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('grandeza', models.CharField(choices=[('Un', 'Unidade'), ('Kg', 'kilograma'), ('L', 'litros')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(blank=True, decimal_places=3, max_digits=21, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('fornecedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materia_prima.fornecedores')),
                ('producao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producao.producao')),
                ('tipo_insumo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materia_prima.insumos')),
            ],
        ),
    ]
