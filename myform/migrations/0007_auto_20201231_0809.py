# Generated by Django 3.1.4 on 2020-12-31 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0006_auto_20201231_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textanswer',
            name='answer_text',
            field=models.CharField(max_length=250),
        ),
    ]
