# Generated by Django 3.2.8 on 2021-11-02 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0003_auto_20211101_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='format',
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=500, verbose_name='Directed by'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='protagonist',
            field=models.CharField(max_length=500, verbose_name='Protagonists'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='synthesis',
            field=models.TextField(max_length=1000, verbose_name='Movie Synthesis'),
        ),
    ]