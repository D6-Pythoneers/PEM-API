# Generated by Django 3.2.9 on 2021-12-10 20:37

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('role', models.CharField(blank=True, choices=[('teacher', 'Teacher'), ('manager', 'Manager')], max_length=250)),
                ('school_id', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('nid', models.BigIntegerField(blank=True, null=True)),
                ('eid', models.BigIntegerField(blank=True, null=True)),
                ('qualification', models.CharField(blank=True, choices=[('diploma', 'Diploma'), ('bachelor', 'Bachelor'), ('masters', 'Masters'), ('phd', 'PhD')], max_length=256, null=True)),
                ('directorate', models.CharField(blank=True, choices=[('amman1', 'Directorate of Amman 1'), ('amman2', 'Directorate of Amman 2'), ('amman3', 'Directorate of Amman 3'), ('amman4', 'Directorate of Amman 4')], max_length=256, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'appUser',
                'verbose_name_plural': 'appUsers',
                'db_table': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
