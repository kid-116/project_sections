# Generated by Django 3.1.6 on 2021-02-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0010_auto_20210221_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='thumb',
            field=models.ImageField(blank='true', default='default.jpsg', upload_to=''),
        ),
    ]