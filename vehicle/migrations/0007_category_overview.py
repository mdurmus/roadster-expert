# Generated by Django 5.0.3 on 2024-03-20 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0006_alter_vehicle_author_delete_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='overview',
            field=models.TextField(blank=True),
        ),
    ]
