# Generated by Django 2.1.9 on 2019-06-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scripts',
            fields=[
                ('script_id', models.IntegerField(primary_key=True, serialize=False)),
                ('script_name', models.CharField(default='', max_length=100)),
                ('script_path', models.CharField(default='', max_length=200)),
                ('script_type', models.IntegerField(default=0)),
                ('type_name', models.CharField(default='', max_length=50)),
                ('script_env', models.CharField(default='', max_length=50)),
                ('create_time', models.DateTimeField(default='2012-12-12 12:12:12')),
                ('update_time', models.DateTimeField(default='2012-12-12 12:12:12')),
            ],
        ),
    ]
