# Generated by Django 3.2 on 2021-06-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210610_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=30)),
                ('phone', models.IntegerField(default='', max_length=12)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
