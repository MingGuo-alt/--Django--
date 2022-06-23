# Generated by Django 4.0.3 on 2022-06-06 10:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=datetime.datetime(2022, 6, 6, 10, 42, 55, 829283, tzinfo=utc), verbose_name='入职时间')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('account', models.CharField(max_length=16, verbose_name='账号')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('job', models.CharField(max_length=10, verbose_name='职位')),
            ],
            options={
                'db_table': 't_Admin',
            },
        ),
        migrations.CreateModel(
            name='General_Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=datetime.datetime(2022, 6, 6, 10, 42, 55, 830281, tzinfo=utc), verbose_name='入职时间')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('account', models.CharField(max_length=16, verbose_name='账号')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('job', models.CharField(max_length=10, verbose_name='职位')),
            ],
            options={
                'db_table': 't_General_Manager',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=datetime.datetime(2022, 6, 6, 10, 42, 55, 828285, tzinfo=utc), verbose_name='入库时间')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('telephone', models.CharField(max_length=11, verbose_name='电话号码')),
                ('note', models.TextField(blank=True, max_length=500, null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 't_users',
            },
        ),
        migrations.CreateModel(
            name='Users_Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=datetime.datetime(2022, 6, 6, 10, 42, 55, 829283, tzinfo=utc), verbose_name='入库时间')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('telephone', models.CharField(max_length=11, verbose_name='电话号码')),
                ('Conversation_record', models.TextField(blank=True, max_length=1000, null=True, verbose_name='洽谈记录')),
            ],
            options={
                'db_table': 't_users_conversation',
            },
        ),
        migrations.CreateModel(
            name='War_Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='战区名称')),
            ],
            options={
                'db_table': 't_war_zone',
            },
        ),
        migrations.CreateModel(
            name='SalesDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=datetime.datetime(2022, 6, 6, 10, 42, 55, 829283, tzinfo=utc), verbose_name='入职时间')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('account', models.CharField(max_length=16, verbose_name='账号')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('job', models.CharField(max_length=10, verbose_name='职位')),
                ('war_zone', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_war_zone', to='Users.war_zone')),
            ],
            options={
                'db_table': 't_Sales_Director',
            },
        ),
        migrations.CreateModel(
            name='Sales_Depart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='销售部门名称')),
                ('war_zone', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_sales_depart', to='Users.war_zone')),
            ],
            options={
                'db_table': 't_sales_depart',
            },
        ),
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=datetime.datetime(2022, 6, 6, 10, 42, 55, 828285, tzinfo=utc), verbose_name='入职时间')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('account', models.CharField(max_length=16, verbose_name='账号')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('job', models.CharField(max_length=10, verbose_name='职位')),
                ('sales_depart', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_sales', to='Users.sales_depart')),
            ],
            options={
                'db_table': 't_sales',
            },
        ),
        migrations.CreateModel(
            name='Job_Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=datetime.datetime(2022, 6, 6, 10, 42, 55, 830281, tzinfo=utc), verbose_name='日志创建时间')),
                ('tel_count', models.IntegerField(verbose_name='打电话数')),
                ('effective_tel_count', models.IntegerField(verbose_name='有效电话数')),
                ('purpose_customer', models.IntegerField(verbose_name='意向客户数')),
                ('interview_customer', models.IntegerField(verbose_name='面谈客户数')),
                ('sales_name', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_job_log', to='Users.sales')),
            ],
            options={
                'db_table': 't_Job_Log',
            },
        ),
        migrations.CreateModel(
            name='Effictive_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=datetime.datetime(2022, 6, 6, 10, 42, 55, 830281, tzinfo=utc), verbose_name='入库时间')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('telephone', models.CharField(max_length=11, verbose_name='电话号码')),
                ('contract_amount', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='合同金额')),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='发放金额')),
                ('sales_name', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_effective_users', to='Users.sales')),
            ],
            options={
                'db_table': 't_effictive_users',
            },
        ),
        migrations.CreateModel(
            name='DepartManger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=datetime.datetime(2022, 6, 6, 10, 42, 55, 829283, tzinfo=utc), verbose_name='入职时间')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('account', models.CharField(max_length=16, verbose_name='账号')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('job', models.CharField(max_length=10, verbose_name='职位')),
                ('sales_depart', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_depart_manger', to='Users.sales_depart')),
            ],
            options={
                'db_table': 't_depart_manger',
            },
        ),
    ]