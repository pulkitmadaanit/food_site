# Generated by Django 3.1 on 2020-09-28 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://kuechentipps.de/wp-content/plugins/osetin-helper/assets/img/placeholder-category.png', max_length=500),
        ),
    ]
