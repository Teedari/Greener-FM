# Generated by Django 3.2.7 on 2021-09-28 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greener', '0002_auto_20210928_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='days',
            field=models.CharField(blank=True, choices=[('sun', 'sunday'), ('mon', 'monday'), ('tue', 'tuesday'), ('wed', 'wednesday'), ('thurs', 'thursday'), ('fri', 'friday'), ('sat', 'saturday')], default='sun', max_length=20),
        ),
    ]