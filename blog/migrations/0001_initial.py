# Generated by Django 3.2 on 2021-07-13 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TitlePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('head0', models.CharField(default='', max_length=500)),
                ('chead0', models.CharField(default='', max_length=5000)),
                ('head1', models.CharField(default='', max_length=500)),
                ('chead1', models.CharField(default='', max_length=5000)),
                ('head2', models.CharField(default='', max_length=500)),
                ('chead2', models.CharField(default='', max_length=5000)),
                ('head3', models.CharField(default='', max_length=500)),
                ('chead3', models.CharField(default='', max_length=5000)),
                ('pub_date', models.DateField()),
                ('Thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]