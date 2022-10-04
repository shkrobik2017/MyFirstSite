# Generated by Django 4.0.5 on 2022-09-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('context', models.TextField(blank=True)),
                ('data', models.DateTimeField(auto_now=True)),
                ('price', models.CharField(max_length=50)),
                ('is_exist', models.BooleanField(default=True)),
            ],
        ),
    ]