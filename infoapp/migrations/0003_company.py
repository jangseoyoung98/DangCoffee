# Generated by Django 4.1 on 2022-08-19 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoapp', '0002_info_list_product_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
