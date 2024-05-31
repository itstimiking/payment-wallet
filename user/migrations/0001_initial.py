# Generated by Django 5.0.6 on 2024-05-24 22:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('bio', models.TextField(blank=True, default='', max_length=225)),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('x', 'Prefer not to say')], default='x', max_length=2)),
                ('avatar', models.CharField(blank=True, default='', max_length=225, null=True)),
                ('banner', models.CharField(blank=True, default='', max_length=225, null=True)),
                ('status', models.CharField(blank=True, default='', max_length=225, null=True)),
                ('online', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('login_login', models.DateTimeField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]