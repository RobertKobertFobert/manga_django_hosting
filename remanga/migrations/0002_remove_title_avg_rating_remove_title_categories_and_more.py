# Generated by Django 4.2.1 on 2023-12-01 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remanga', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='avg_rating',
        ),
        migrations.RemoveField(
            model_name='title',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='title',
            name='chapters',
        ),
        migrations.RemoveField(
            model_name='title',
            name='count_bookmarks',
        ),
        migrations.RemoveField(
            model_name='title',
            name='count_chapters',
        ),
        migrations.RemoveField(
            model_name='title',
            name='count_rating',
        ),
        migrations.RemoveField(
            model_name='title',
            name='description',
        ),
        migrations.RemoveField(
            model_name='title',
            name='dir_name',
        ),
        migrations.RemoveField(
            model_name='title',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='title',
            name='img_url',
        ),
        migrations.RemoveField(
            model_name='title',
            name='issue_year',
        ),
        migrations.RemoveField(
            model_name='title',
            name='manga_type',
        ),
        migrations.RemoveField(
            model_name='title',
            name='rus_name',
        ),
        migrations.RemoveField(
            model_name='title',
            name='total_views',
        ),
        migrations.RemoveField(
            model_name='title',
            name='total_votes',
        ),
    ]
