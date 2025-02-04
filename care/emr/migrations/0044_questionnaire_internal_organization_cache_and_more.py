# Generated by Django 5.1.3 on 2024-12-25 17:51

import django.contrib.postgres.fields
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0043_facilityorganization_cached_parent_json'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='internal_organization_cache',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='organization_cache',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
        migrations.CreateModel(
            name='QuestionnaireFacilityOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.facilityorganization')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.questionnaire')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionnaireOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.organization')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.questionnaire')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
