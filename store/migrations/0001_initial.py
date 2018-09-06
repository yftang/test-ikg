# Generated by Django 2.0.7 on 2018-07-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['category'], name='category_idx'),
        ),
    ]