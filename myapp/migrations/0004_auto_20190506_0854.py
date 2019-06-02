# Generated by Django 2.2 on 2019-05-06 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190505_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('draft', 'DRAFT'), ('published', 'PUBLISHED')], default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%M/'),
        ),
    ]