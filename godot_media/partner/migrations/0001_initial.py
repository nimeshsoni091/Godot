# Generated by Django 3.2.8 on 2021-10-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('gst', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=60)),
                ('agency', models.CharField(max_length=60)),
            ],
        ),
    ]