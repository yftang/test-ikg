# Generated by Django 2.0.7 on 2018-07-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distributor',
            options={'ordering': ('slug',)},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('category', 'slug')},
        ),
        migrations.AddField(
            model_name='product',
            name='distributors',
            field=models.ManyToManyField(to='store.Distributor'),
        ),
    ]
