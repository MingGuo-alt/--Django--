import os
from decimal import Decimal

from django.db import models
from django.utils import timezone as datetime

# Create your models here.

import uuid
#提取出公共的方法evaluation_directory_path获取图片后缀
# 使用uuid创建唯一的图片名，并保存的路径和文件名一并返回
def evaluation_directory_path(product_id, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("img", filename)

def contract_directory_path(product_id, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("contract", filename)

class War_Zone(models.Model):
    """战区表"""
    name = models.CharField(max_length=50,verbose_name="战区名称")

    class Meta:
        db_table = "t_war_zone"

    def __str__(self):
        return self.name

class Sales_Depart(models.Model):
    """销售部门表"""
    name = models.CharField(max_length=50,verbose_name="销售部门名称")
    war_zone = models.ForeignKey(War_Zone,on_delete=models.DO_NOTHING,related_name="c_sales_depart",db_constraint=False)

    class Meta:
        db_table = "t_sales_depart"

    def __str__(self):
        return self.name

class Users(models.Model):
    """
    公海库表
    """
    name = models.CharField(max_length=50,verbose_name="姓名")
    age = models.SmallIntegerField(verbose_name="年龄")
    sex = models.CharField(max_length=2,verbose_name="性别") #性别，默认为真=男性
    telephone = models.CharField(max_length=11,verbose_name="电话号码")
    create_time = models.DateTimeField(auto_created=datetime.now(),verbose_name="入库时间")
    note = models.TextField(max_length=500,verbose_name="备注",blank=True,null=True)

    class Meta:
        db_table = "t_users"

    def __str__(self):
        return self.name

class sales(models.Model):
    """
    销售代表表
    """
    name = models.CharField(max_length=50, verbose_name="姓名")
    sex = models.CharField(max_length=2, verbose_name="性别")  # 性别，默认为真=男性
    account = models.CharField(max_length=16,verbose_name="账号")
    password = models.CharField(max_length=100,verbose_name="密码")
    create_time = models.DateTimeField(auto_created=datetime.now(),verbose_name="入职时间")
    job = models.CharField(max_length=10,verbose_name="职位")
    sales_depart = models.ForeignKey(Sales_Depart,on_delete=models.DO_NOTHING,related_name="c_sales",db_constraint=False)
    # war_zone = models.ForeignKey(War_Zone,on_delete=models.DO_NOTHING,related_name="s_sales",db_constraint=False)

    class Meta:
        db_table = "t_sales"

    def __str__(self):
        return self.name

class DepartManger(models.Model):
    """
    部门经理
    """
    name = models.CharField(max_length=50, verbose_name="姓名")
    sex = models.CharField(max_length=2, verbose_name="性别")  # 性别，默认为真=男性
    account = models.CharField(max_length=16,verbose_name="账号")
    password = models.CharField(max_length=100,verbose_name="密码")
    create_time = models.DateTimeField(auto_created=datetime.now(),verbose_name="入职时间")
    job = models.CharField(max_length=10,verbose_name="职位")
    sales_depart = models.ForeignKey(Sales_Depart,on_delete=models.DO_NOTHING,related_name="c_depart_manger",db_constraint=False)
    # war_zone = models.ForeignKey(War_Zone,on_delete=models.DO_NOTHING,related_name="s_sales",db_constraint=False)

    class Meta:
        db_table = "t_depart_manger"

    def __str__(self):
        return self.name

class Users_Conversation(models.Model):
    """洽谈记录表"""
    name = models.CharField(max_length=50, verbose_name="姓名")
    age = models.SmallIntegerField(verbose_name="年龄")
    sex = models.CharField(max_length=2, verbose_name="性别")  # 性别，默认为真=男性
    telephone = models.CharField(max_length=11, verbose_name="电话号码")
    create_time = models.DateTimeField(auto_created=datetime.now(), verbose_name="入库时间")
    Conversation_record = models.TextField(max_length=1000, verbose_name="洽谈记录", blank=True, null=True)
    loan_money = models.IntegerField(verbose_name="贷款意向金额",default="0")
    sales_name = models.ForeignKey(sales, on_delete=models.DO_NOTHING, related_name="c_users_conversation", db_constraint=False,default="2")

    class Meta:
        db_table = "t_users_conversation"

    def __str__(self):
        return self.name

class SalesDirector(models.Model):
    """销售总监"""
    name = models.CharField(max_length=50, verbose_name="姓名")
    sex = models.CharField(max_length=2, verbose_name="性别")  # 性别，默认为真=男性
    account = models.CharField(max_length=16, verbose_name="账号")
    password = models.CharField(max_length=100, verbose_name="密码")
    create_time = models.DateTimeField(auto_created=datetime.now(), verbose_name="入职时间")
    job = models.CharField(max_length=10, verbose_name="职位")
    war_zone = models.ForeignKey(War_Zone, on_delete=models.DO_NOTHING, related_name="c_war_zone", db_constraint=False)

    class Meta:
        db_table = "t_Sales_Director"

    def __str__(self):
        return self.name

class Admin(models.Model):
    """系统管理员"""
    name = models.CharField(max_length=50, verbose_name="姓名")
    sex = models.CharField(max_length=2, verbose_name="性别")  # 性别，默认为真=男性
    account = models.CharField(max_length=16, verbose_name="账号")
    password = models.CharField(max_length=100, verbose_name="密码")
    create_time = models.DateTimeField(auto_created=datetime.now(), verbose_name="入职时间")
    job = models.CharField(max_length=10, verbose_name="职位")

    class Meta:
        db_table = "t_Admin"

    def __str__(self):
        return self.name

class General_Manager(models.Model):
    """总经理"""
    name = models.CharField(max_length=50, verbose_name="姓名")
    sex = models.CharField(max_length=2, verbose_name="性别")  # 性别，默认为真=男性
    account = models.CharField(max_length=16, verbose_name="账号")
    password = models.CharField(max_length=100, verbose_name="密码")
    create_time = models.DateTimeField(auto_created=datetime.now(), verbose_name="入职时间")
    job = models.CharField(max_length=10, verbose_name="职位")

    class Meta:
        db_table = "t_General_Manager"

    def __str__(self):
        return self.name

class Job_Log(models.Model):
    """工作日志"""
    tel_count = models.IntegerField(verbose_name="打电话数")
    effective_tel_count = models.IntegerField(verbose_name="有效电话数")
    purpose_customer = models.IntegerField(verbose_name="意向客户数")
    interview_customer = models.IntegerField(verbose_name="面谈客户数")
    create_time = models.DateTimeField(auto_created=datetime.now(), verbose_name="日志创建时间")
    sales_name = models.ForeignKey(sales,on_delete=models.DO_NOTHING,related_name="c_job_log",db_constraint=False)

    class Meta:
        db_table = "t_Job_Log"

    def __str__(self):
        return self.sales_name

class Effictive_Users(models.Model):
    """
    销售代表达成合同的客户数
    """
    name = models.CharField(max_length=50,verbose_name="姓名")
    age = models.SmallIntegerField(verbose_name="年龄")
    sex = models.CharField(max_length=2,verbose_name="性别") #性别，默认为真=男性
    telephone = models.CharField(max_length=11,verbose_name="电话号码")
    job = models.CharField(max_length=11,verbose_name="职业",default="xxx")
    create_time = models.DateTimeField(auto_created=datetime.now(),verbose_name="入库时间")
    order_status = models.CharField(max_length=20,verbose_name="订单状态",default="订单审核中")
    contract_amount = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="合同金额")
    loan_amount = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="发放金额")
    sales_name = models.ForeignKey(sales,on_delete=models.DO_NOTHING,related_name="c_effective_users",db_constraint=False)
    img_id_card = models.ImageField(upload_to=evaluation_directory_path,verbose_name='身份证',null=True,blank=True)
    check_status = models.BooleanField(default=False,verbose_name="贷款下放") # False = 0 True = 1
    contract_number = models.CharField(max_length=100,verbose_name="合同编号",default="xxx")
    service_fee_number = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="服务费",null=True,blank=True)
    service_fee_status = models.CharField(max_length=10,verbose_name="是否收取服务费",default="未收取") # False = 0 True = 1
    note = models.TextField(max_length=1000,verbose_name="备注",null=True,blank=True)

    class Meta:
        db_table = "t_effictive_users"

    def __str__(self):
        return self.name

class OpLogs(models.Model):
    """操作日志表"""
    re_time = models.CharField(max_length=32, verbose_name='请求时间')
    # re_user = models.CharField(max_length=32, verbose_name='操作人')
    re_ip = models.CharField(max_length=32, verbose_name='请求IP')
    re_url = models.CharField(max_length=255, verbose_name='请求url')
    re_method = models.CharField(max_length=11, verbose_name='请求方法')
    re_content = models.TextField(null=True, verbose_name='请求参数')
    rp_content = models.TextField(null=True, verbose_name='响应参数')
    access_time = models.IntegerField(verbose_name='响应耗时/ms')

    class Meta:
        db_table = 'op_logs'


class AccessTimeOutLogs(models.Model):
    """超时操作日志表"""
    re_time = models.CharField(max_length=32, verbose_name='请求时间')
    # re_user = models.CharField(max_length=32, verbose_name='操作人')
    re_ip = models.CharField(max_length=32, verbose_name='请求IP')
    re_url = models.CharField(max_length=255, verbose_name='请求url')
    re_method = models.CharField(max_length=11, verbose_name='请求方法')
    re_content = models.TextField(null=True, verbose_name='请求参数')
    rp_content = models.TextField(null=True, verbose_name='响应参数')
    access_time = models.IntegerField(verbose_name='响应耗时/ms')

    class Meta:
        db_table = 'access_timeout_logs'

class Financial_Commissioner(models.Model):
    """金融专员"""
    name = models.CharField(max_length=50, verbose_name="姓名")
    sex = models.CharField(max_length=2, verbose_name="性别")
    account = models.CharField(max_length=16, verbose_name="账号")
    password = models.CharField(max_length=100, verbose_name="密码")
    create_time = models.DateTimeField(auto_created=datetime.now(), verbose_name="入职时间")
    job = models.CharField(max_length=10, verbose_name="职位")

    class Meta:
        db_table = "t_financial_commissioner"

    def __str__(self):
        return self.name

class Performance(models.Model):
    """销售业绩"""
    sale_name = models.CharField(max_length=50, verbose_name="姓名")
    contract_amount_total = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="合同金额")

    class Meta:
        db_table = "t_performance"

    def __str__(self):
        return self.sale_name

class Contract(models.Model):
    """合同"""
    contract_name = models.CharField(max_length=50,verbose_name="合同名称")
    contract_number = models.CharField(max_length=100,verbose_name="合同编号",default="xxx")
    contract_time = models.DateTimeField(auto_created=datetime.now(), verbose_name="合同上传时间")
    contract_money = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="合同金额")
    contract_image = models.ImageField(upload_to=contract_directory_path,verbose_name='合同照片',null=True,blank=True)
    effictiveusers_id = models.ForeignKey(Effictive_Users,on_delete=models.DO_NOTHING,related_name="c_Contract",db_constraint=False)

    class Meta:
        db_table = "t_contract"

    def __str__(self):
        return self.contract_name

class Accountant(models.Model):
    """会计"""
    name = models.CharField(max_length=50, verbose_name="姓名")
    sex = models.CharField(max_length=2, verbose_name="性别")
    account = models.CharField(max_length=16, verbose_name="账号")
    password = models.CharField(max_length=100, verbose_name="密码")
    create_time = models.DateTimeField(auto_created=datetime.now(), verbose_name="入职时间")
    job = models.CharField(max_length=10, verbose_name="职位")

    class Meta:
        db_table = "t_accountant"

    def __str__(self):
        return self.name