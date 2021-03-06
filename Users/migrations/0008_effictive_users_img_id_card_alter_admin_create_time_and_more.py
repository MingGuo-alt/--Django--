# Generated by Django 4.0.3 on 2022-06-08 06:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_performance_alter_admin_create_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='effictive_users',
            name='img_id_card',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='身份证'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 8, 6, 49, 3, 148888, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='departmanger',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 8, 6, 49, 3, 147887, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='effictive_users',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 8, 6, 49, 3, 149894, tzinfo=utc), verbose_name='入库时间'),
        ),
        migrations.AlterField(
            model_name='financial_commissioner',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 8, 6, 49, 3, 150884, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='general_manager',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 8, 6, 49, 3, 149894, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='job_log',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 8, 6, 49, 3, 149894, tzinfo=utc), verbose_name='日志创建时间'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 8, 6, 49, 3, 147887, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='salesdirector',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 8, 6, 49, 3, 148888, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='users',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 8, 6, 49, 3, 147887, tzinfo=utc), verbose_name='入库时间'),
        ),
        migrations.AlterField(
            model_name='users_conversation',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 8, 6, 49, 3, 148888, tzinfo=utc), verbose_name='入库时间'),
        ),
    ]
