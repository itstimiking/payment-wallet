# Generated by Django 5.0.6 on 2024-05-26 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_walletmodel_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walletmodel',
            old_name='user_id',
            new_name='user',
        ),
    ]
