# Generated by Django 2.0 on 2019-07-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=1000)),
                ('name_product_subs', models.CharField(max_length=1000)),
                ('prod_sub_nut', models.CharField(max_length=1000)),
                ('nut_100', models.TextField()),
                ('nut_levels', models.TextField()),
                ('image_product', models.CharField(max_length=2000)),
                ('image_product_subs', models.CharField(max_length=2000)),
                ('cuurent_user', models.IntegerField()),
                ('url_subs', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Product_subs',
            },
        ),
    ]
