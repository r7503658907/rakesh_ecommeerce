# Generated by Django 4.0.6 on 2023-01-11 05:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0014_product_bestseller_product_toprate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='viewEvevnt',
            fields=[
                ('viewId', models.AutoField(primary_key=True, serialize=False)),
                ('dateTime', models.DateTimeField(default=datetime.datetime(2023, 1, 11, 10, 46, 24, 651182))),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
