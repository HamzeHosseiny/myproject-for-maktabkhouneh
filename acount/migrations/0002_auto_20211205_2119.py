# Generated by Django 3.2.8 on 2021-12-05 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='billing_city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='billing_country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='billing_state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='billing_zip_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='credit_card_expiration_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='credit_card_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='credit_card_security_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='credit_card_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shipping_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shipping_city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shipping_country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shipping_state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shipping_zip_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='zip_code',
        ),
    ]
