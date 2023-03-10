# Generated by Django 4.0.6 on 2023-01-10 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_profile_email_alter_profile_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodayDeals',
            fields=[
                ('dealId', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(default=0, max_length=100)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.product')),
            ],
        ),
    ]
