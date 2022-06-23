# Generated by Django 4.0.3 on 2022-06-15 02:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_effictive_users_note_alter_accountant_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountant',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 374095, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 371110, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 373099, tzinfo=utc), verbose_name='合同上传时间'),
        ),
        migrations.AlterField(
            model_name='departmanger',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 370114, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='effictive_users',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 372111, tzinfo=utc), verbose_name='入库时间'),
        ),
        migrations.AlterField(
            model_name='effictive_users',
            name='service_fee_status',
            field=models.CharField(default='未收取', max_length=10, verbose_name='是否收取服务费'),
        ),
        migrations.AlterField(
            model_name='financial_commissioner',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 373099, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='general_manager',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 372111, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='job_log',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 372111, tzinfo=utc), verbose_name='日志创建时间'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 370114, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='salesdirector',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 371110, tzinfo=utc), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='users',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 370114, tzinfo=utc), verbose_name='入库时间'),
        ),
        migrations.AlterField(
            model_name='users_conversation',
            name='create_time',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 6, 15, 2, 27, 16, 371110, tzinfo=utc), verbose_name='入库时间'),
        ),
    ]
