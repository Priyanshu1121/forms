# Generated by Django 3.1.4 on 2021-01-03 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0010_auto_20210103_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boolanswer',
            name='user_id',
        ),
    ]