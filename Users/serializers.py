from rest_framework import serializers
from .models import Users, Users_Conversation,sales,War_Zone,Sales_Depart,DepartManger,SalesDirector
from .models import Admin, General_Manager
from .models import Job_Log, Effictive_Users, OpLogs
from .models import Financial_Commissioner,Performance,Contract,Accountant

class UserModelSerializer(serializers.ModelSerializer):
    """
        用公海数据库序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Users
        fields = "__all__"

class UsersConversationModelSerializer(serializers.ModelSerializer):
    """
    用户洽谈记录序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Users_Conversation
        fields = "__all__"

    def to_representation(self, instance):
        ret_obj = super().to_representation(instance)
        ret_obj['sales_name'] = SaleModelSerializer(instance=instance.sales_name).data
        print(instance.sales_name)
        return ret_obj

class SaleModelSerializer(serializers.ModelSerializer):
    """
        公司内部销售人员外键级联序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = sales
        fields = ["id", "name", "sex", "account", "create_time", "job", "sales_depart"]
    def to_representation(self, instance):
        ret_obj = super().to_representation(instance)
        ret_obj['sales_depart'] = SalesDepartModelSerializer(instance=instance.sales_depart).data
        ret_obj['war_zone'] = WarZoneModelSerializer(instance=instance.sales_depart.war_zone).data
        return ret_obj
    # depth = 2

class SaleLoginRegisterModelSerializer(serializers.ModelSerializer):
    """
        销售代表序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = sales
        fields = "__all__"

class DepartModelSerializer(serializers.ModelSerializer):
    """
        部门经理外键级联序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = DepartManger
        fields = ["id", "name", "sex", "account", "create_time", "job", "sales_depart"]

    def to_representation(self, instance):
        ret_obj = super().to_representation(instance)
        ret_obj['sales_depart'] = SalesDepartModelSerializer(instance=instance.sales_depart).data
        ret_obj['war_zone'] = WarZoneModelSerializer(instance=instance.sales_depart.war_zone).data
        return ret_obj

class DepartMangerLoginRegisterModelSerializer(serializers.ModelSerializer):
    """
        部门经理登录注册序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = DepartManger
        fields = "__all__"

class SalesDirectorModelSerializer(serializers.ModelSerializer):
    """
        销售总监外键级联序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = SalesDirector
        fields = ["id", "name", "sex", "account", "create_time", "job", "war_zone"]

    def to_representation(self, instance):
        ret_obj = super().to_representation(instance)
        ret_obj['war_zone'] = WarZoneModelSerializer(instance=instance.war_zone).data
        return ret_obj

class SalesDirectoLoginRegisterModelSerializer(serializers.ModelSerializer):
    """
        部门经理登录注册序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = SalesDirector
        fields = "__all__"

class WarZoneModelSerializer(serializers.ModelSerializer):
    """
        战区序列化器
    """
    class Meta:
        model = War_Zone
        fields = "__all__"

class SalesDepartModelSerializer(serializers.ModelSerializer):
    """
        销售部门序列化器
    """
    class Meta:
        model = Sales_Depart
        fields = "__all__"

    def to_representation(self, instance):
        ret_obj = super().to_representation(instance)
        ret_obj['war_zone'] = WarZoneModelSerializer(instance=instance.war_zone).data
        # print(instance.sales_name)
        return ret_obj

class AdminModelSerializer(serializers.ModelSerializer):
    """
        系统管理员序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Admin
        fields = "__all__"

class AdminLoginRegisterModelSerializer(serializers.ModelSerializer):
    """
        系统管理员登录功能序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Admin
        fields = "__all__"

class GeneralManagerModelSerializer(serializers.ModelSerializer):
    """
        总经理序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = General_Manager
        fields = "__all__"

class GeneralManagerRegisterModelSerializer(serializers.ModelSerializer):
    """
        总经理登录注册功能序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = General_Manager
        fields = "__all__"

class JobLogModelSerializer(serializers.ModelSerializer):
    """
        工作日志
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Job_Log
        fields = "__all__"

    def to_representation(self, instance):
        ret_obj = super().to_representation(instance)
        ret_obj['sales_name'] = SaleModelSerializer(instance=instance.sales_name).data
        print(instance.sales_name)
        return ret_obj

class EffictiveUsersModelSerializer(serializers.ModelSerializer):
    """
        签约用户
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Effictive_Users
        fields = "__all__"

    def to_representation(self, instance):
        ret_obj = super().to_representation(instance)
        ret_obj['sales_name'] = SaleModelSerializer(instance=instance.sales_name).data
        # print(instance.sales_name)
        return ret_obj

class OpLogsModelSerializer(serializers.ModelSerializer):
    """
        日操作志数据库
    """
    # create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = OpLogs
        fields = "__all__"

class FinancialCommissionModelSerializer(serializers.ModelSerializer):
    """
        系统管理员序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Financial_Commissioner
        fields = "__all__"

class PerformanceModelSerializer(serializers.ModelSerializer):
    """
        工作日志
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Performance
        fields = "__all__"

class ContractModelSerializer(serializers.ModelSerializer):
    """
        合同
    """
    contract_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Contract
        fields = "__all__"

    def to_representation(self, instance):
        ret_obj = super().to_representation(instance)
        ret_obj['effictiveusers_id'] = EffictiveUsersModelSerializer(instance=instance.effictiveusers_id).data
        return ret_obj

class AccountantModelSerializer(serializers.ModelSerializer):
    """
        会计登录注册功能序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Accountant
        fields = "__all__"