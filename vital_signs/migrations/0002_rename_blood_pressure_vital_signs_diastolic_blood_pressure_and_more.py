# Generated by Django 4.2 on 2024-10-10 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vital_signs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vital_signs',
            old_name='blood_pressure',
            new_name='diastolic_blood_pressure',
        ),
        migrations.AddField(
            model_name='vital_signs',
            name='systolic_blood_pressure',
            field=models.DecimalField(decimal_places=2, default=120, max_digits=5),
            preserve_default=False,
        ),
    ]
