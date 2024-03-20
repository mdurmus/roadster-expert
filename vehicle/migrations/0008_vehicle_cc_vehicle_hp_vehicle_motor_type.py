# Generated by Django 5.0.3 on 2024-03-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_category_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='cc',
            field=models.CharField(default='5000', max_length=5),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='hp',
            field=models.CharField(default='10000', max_length=5),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='motor_type',
            field=models.CharField(default='Boxer', max_length=20),
        ),
    ]
