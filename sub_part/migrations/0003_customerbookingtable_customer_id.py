# Generated by Django 5.1.5 on 2025-03-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_customerbookingtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerbookingtable',
            name='customer_id',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
