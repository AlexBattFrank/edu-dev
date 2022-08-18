# Generated by Django 4.1 on 2022-08-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_rename_text_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoryType',
            field=models.CharField(choices=[('NW', 'One String News'), ('AR', 'Articles'), ('REG', 'REG'), ('POL', 'POL'), ('SAT', 'SAT')], default='AR', max_length=4),
        ),
    ]
