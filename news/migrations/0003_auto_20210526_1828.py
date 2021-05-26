# Generated by Django 3.1.4 on 2021-05-26 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_title_url'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together={('title', 'image', 'title_url', 'summary', 'tag')},
        ),
    ]
