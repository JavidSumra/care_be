# Generated by Django 5.1.3 on 2024-12-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0039_facilityorganization_root_org_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilityorganization',
            name='has_children',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='has_children',
            field=models.BooleanField(default=False),
        ),
    ]
