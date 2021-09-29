# Generated by Django 3.2.7 on 2021-09-28 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('greener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='host',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='authentication.profile'),
        ),
    ]
