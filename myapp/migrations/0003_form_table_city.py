# Generated by Django 4.2.5 on 2023-11-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_form_table_age_alter_form_table_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_table',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
    ]