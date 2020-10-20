# Generated by Django 3.1 on 2020-09-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('role', models.CharField(max_length=90)),
            ],
        ),
        migrations.DeleteModel(
            name='data',
        ),
    ]