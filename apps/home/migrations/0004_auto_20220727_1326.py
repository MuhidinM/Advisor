# Generated by Django 3.2.6 on 2022-07-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_fname_assign_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='advisor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Assign',
        ),
    ]
