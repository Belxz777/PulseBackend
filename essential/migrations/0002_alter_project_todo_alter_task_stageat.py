# Generated by Django 5.0.2 on 2024-04-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essential', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='todo',
            field=models.ManyToManyField(blank=True, to='essential.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='stageAt',
            field=models.CharField(choices=[('G', 'Готово'), ('R', 'В процессе'), ('O', 'В обсуждении')], default='O', max_length=20),
        ),
    ]