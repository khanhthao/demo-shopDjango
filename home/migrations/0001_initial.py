# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group_permissions',
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_permission',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.BooleanField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('username', models.CharField(unique=True, max_length=150)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_groups',
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_user_permissions',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.IntegerField(serialize=False, primary_key=True)),
                ('cate_parent_id', models.IntegerField(null=True, blank=True)),
                ('cate_name', models.TextField(null=True, blank=True)),
                ('cate_description', models.TextField(null=True, blank=True)),
                ('cate_status', models.NullBooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(serialize=False, primary_key=True, max_length=40)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_session',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(serialize=False, primary_key=True)),
                ('ship_name', models.TextField(null=True, blank=True)),
                ('ship_address', models.TextField(null=True, blank=True)),
                ('ship_phone', models.TextField(null=True, blank=True)),
                ('ordered_date', models.DateTimeField(null=True, blank=True)),
                ('total_amount', models.TextField(null=True, blank=True)),
                ('order_status', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('order_detail_id', models.IntegerField(serialize=False, primary_key=True)),
                ('order_id', models.IntegerField(null=True, blank=True)),
                ('product_id', models.IntegerField(null=True, blank=True)),
                ('product_price', models.TextField(null=True, blank=True)),
                ('product_quantity', models.IntegerField(null=True, blank=True)),
                ('amount', models.TextField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Order_Detail',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(serialize=False, primary_key=True)),
                ('cate_id', models.IntegerField(null=True, blank=True)),
                ('product_name', models.IntegerField(null=True, blank=True)),
                ('product_price', models.TextField(null=True, blank=True)),
                ('product_quantity', models.IntegerField(null=True, blank=True)),
                ('product_image', models.TextField(null=True, blank=True)),
                ('product_detail', models.TextField(null=True, blank=True)),
                ('product_status', models.NullBooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('image_id', models.IntegerField(serialize=False, primary_key=True)),
                ('product_id', models.IntegerField()),
                ('image_path', models.TextField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Product_Images',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('promotion_id', models.IntegerField(serialize=False, primary_key=True)),
                ('product_id', models.IntegerField(null=True, blank=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('discount', models.TextField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Promotion',
            },
        ),
    ]
