# Generated by Django 2.0.13 on 2019-03-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('realesedate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=10)),
                ('point', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
