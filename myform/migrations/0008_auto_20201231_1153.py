# Generated by Django 3.1.4 on 2020-12-31 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0007_auto_20201231_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='user_id',
        ),
        migrations.AddField(
            model_name='textform',
            name='form_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myform.form'),
            preserve_default=False,
        ),
    ]
