# Generated by Django 2.2 on 2021-02-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('show_name', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除'), (2, '草稿')], default=2)),
            ],
        ),
    ]
