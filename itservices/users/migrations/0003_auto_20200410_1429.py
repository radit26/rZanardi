# Generated by Django 3.0.4 on 2020-04-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200408_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profiles/default.jpg', upload_to='profiles'),
        ),
    ]