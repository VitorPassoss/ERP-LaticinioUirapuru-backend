# Generated by Django 4.0 on 2023-09-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0005_produtoestoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producao',
            name='status',
            field=models.CharField(choices=[('EA', 'Em andamento'), ('F', 'Finalizado'), ('S', 'Saida')], max_length=2),
        ),
    ]
