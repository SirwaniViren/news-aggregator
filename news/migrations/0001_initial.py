# Generated by Django 3.1.4 on 2021-05-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.URLField(blank=True, null=True)),
                ('summary', models.CharField(blank=True, max_length=1000, null=True)),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
    ]
