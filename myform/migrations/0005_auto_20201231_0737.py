# Generated by Django 3.1.4 on 2020-12-31 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0004_remove_textanswer_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textanswer',
            name='answer_text',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
