# Generated by Django 4.1 on 2022-08-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
