# Generated by Django 4.0 on 2023-08-20 21:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('materia_prima', '0004_remove_entrada_producao'),
        ('producao', '0003_remove_produtos_validade_produtos_validade_dias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producaoitem',
            options={},
        ),
        migrations.RemoveField(
            model_name='producaoitem',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='producaoitem',
            name='valor',
        ),
        migrations.AddField(
            model_name='producaoitem',
            name='leite_processado',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=21, null=True),
        ),
        migrations.AlterField(
            model_name='producaoitem',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producao.produtos'),
        ),
        migrations.CreateModel(
            name='ProducaoInsumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(blank=True, decimal_places=3, max_digits=21, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('producao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='producao.producao')),
                ('tipo_insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materia_prima.insumos')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
