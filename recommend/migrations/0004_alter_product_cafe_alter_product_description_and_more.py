# Generated by Django 4.1 on 2022-08-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0003_merge_20220817_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cafe',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='admin/image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Cafe',
        ),
    ]
