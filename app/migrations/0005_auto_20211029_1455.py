# Generated by Django 3.2.8 on 2021-10-29 18:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_pedido_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 10, 29, 18, 55, 35, 865914, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='prato',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 10, 29, 18, 55, 44, 785587, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prato',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
