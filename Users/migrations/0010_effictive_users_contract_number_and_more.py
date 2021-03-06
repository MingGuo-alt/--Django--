# Generated by Django 4.0.3 on 2022-06-09 05:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_effictive_users_check_status_alter_admin_create_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='effictive_users',
            name='contract_number',
            field=models.CharField(default='xxx', max_length=100, verbose_name='合同编号'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 9, 5, 58, 42, 668572, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='departmanger',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 9, 5, 58, 42, 667576, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='effictive_users',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 9, 5, 58, 42, 669570, tzinfo=utc), verbose_name='入库时间'),
        ),
        migrations.AlterField(
            model_name='financial_commissioner',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 9, 5, 58, 42, 670567, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='general_manager',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 9, 5, 58, 42, 669570, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='job_log',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 9, 5, 58, 42, 669570, tzinfo=utc), verbose_name='日志创建时间'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 9, 5, 58, 42, 667576, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='salesdirector',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 9, 5, 58, 42, 668572, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='users',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 9, 5, 58, 42, 667576, tzinfo=utc), verbose_name='入库时间'),
        ),
        migrations.AlterField(
            model_name='users_conversation',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 9, 5, 58, 42, 668572, tzinfo=utc), verbose_name='入库时间'),
        ),
    ]
