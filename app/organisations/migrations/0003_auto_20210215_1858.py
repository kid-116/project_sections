# Generated by Django 3.1.6 on 2021-02-15 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organisations', '0002_auto_20210215_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='administrator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_of', to=settings.AUTH_USER_MODEL),
        ),
    ]
