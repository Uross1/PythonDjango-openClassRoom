# Generated by Django 4.1.3 on 2022-11-16 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_band_active_band_biography_band_official_homepage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='band',
            name='title',
        ),
    ]
