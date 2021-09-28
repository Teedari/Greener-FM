# Generated by Django 3.2.7 on 2021-09-28 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('days', models.CharField(choices=[('sun', 'sunday'), ('mon', 'monday'), ('tue', 'tuesday'), ('wed', 'wednesday'), ('thurs', 'thursday'), ('fri', 'friday'), ('sat', 'saturday')], default='sun', max_length=20)),
                ('time', models.TimeField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('announcement', models.ManyToManyField(related_name='announcements', to='greener.Announcement')),
                ('host', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='authentication.profile')),
                ('sponsorship', models.ManyToManyField(related_name='sponsorships', to='greener.Sponsorship')),
            ],
        ),
    ]