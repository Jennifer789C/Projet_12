# Generated by Django 4.1.6 on 2023-02-27 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_alter_evenement_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='vendeur',
            field=models.ForeignKey(limit_choices_to={'groups': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
