# Generated by Django 2.0.7 on 2018-07-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renewal', '0002_auto_20180711_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]