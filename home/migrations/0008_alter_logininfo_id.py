# Generated by Django 4.2.6 on 2023-10-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191115_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logininfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
