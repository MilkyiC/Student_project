# Generated by Django 5.1.2 on 2024-10-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_course_title_enrollment_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='end_date',
            field=models.DateField(auto_now=True, verbose_name='Дата конца'),
        ),
        migrations.AlterField(
            model_name='book',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Дата начала'),
        ),
    ]
