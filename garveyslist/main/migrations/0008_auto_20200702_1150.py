# Generated by Django 3.0.8 on 2020-07-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200702_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='phone_number',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='business',
            name='website',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='business',
            name='zipcode',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
    ]
