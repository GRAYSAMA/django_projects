# Generated by Django 5.1.7 on 2025-03-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
