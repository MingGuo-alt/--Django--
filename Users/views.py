import decimal
import json

from rest_framework.viewsets import ModelViewSet
from django.db.models import Avg, Max, Min,Count
from django.contrib.auth.hashers import make_password, check_password
from .serializers import UserModelSerializer, UsersConversationModelSerializer, SaleModelSerializer,WarZoneModelSerializer,SalesDepartModelSerializer
from .models import Users, Users_Conversation, sales, War_Zone, Sales_Depart, DepartManger, SalesDirector, \
    Admin,General_Manager,Job_Log,Effictive_Users,OpLogs,Financial_Commissioner,Contract
from rest_framework import generics
from .pagination import UserPageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .filters import NameSearchFilter
from .serializers import SaleLoginRegisterModelSerializer
from .serializers import DepartModelSerializer, DepartMangerLoginRegisterModelSerializer
from .serializers import SalesDirectorModelSerializer, SalesDirectoLoginRegisterModelSerializer
from .serializers import AdminModelSerializer,AdminLoginRegisterModelSerializer
from .serializers import GeneralManagerModelSerializer,GeneralManagerRegisterModelSerializer
from .serializers import JobLogModelSerializer
from .serializers import EffictiveUsersModelSerializer
from .serializers import OpLogsModelSerializer
from .serializers import FinancialCommissionModelSerializer,PerformanceModelSerializer,ContractModelSerializer
from .serializers import Accountant,AccountantModelSerializer


def service_fee(contract_amount):
    """
        计算服务费函数
    :param contract_amount:贷款合同金额
    :return:
    """
    print(type(contract_amount))
    print(contract_amount)
    # service_fee_count = 0
    if float(contract_amount) <= 5:
        service_fee_count = 500
    elif float(contract_amount) <= 10 and float(contract_amount) > 5:
        service_fee_count = 1500
    elif float(contract_amount) >10 and float(contract_amount) <=50:
        service_fee_count = 3000
    else:
        service_fee_count = 5000
    return service_fee_count

class UserView(generics.ListCreateAPIView):
    """
    公海信息库
    GET：得到所有用户信息
    POST：添加用户信息
    """
    queryset = Users.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    公海信息库
    GET/pk/:得到一个用户信息
    PUT/pk/:更新一个用户信息
    DELETE/pk/:删除一个用户信息
    """
    queryset = Users.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class UserConversationView(generics.ListCreateAPIView):
    """
        洽谈记录信息库
        GET：得到所有用户信息
        POST：添加用户信息
        """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据用户id过滤
        前端需要传入一个销售人员ID
        """
        # 从URL获取sales_name参数
        sales_name = self.request.GET.get('sales_name')
        # print(sales_name)
        return Users_Conversation.objects.filter(sales_name=sales_name)

    queryset = Users_Conversation.objects.all()
    serializer_class = UsersConversationModelSerializer
    pagination_class = UserPageNumberPagination  # 局部分页
    filter_backends = [NameSearchFilter]  # 查询功能

class UserConversationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    洽谈记录信息库
    GET/pk/:得到一个用户信息
    PUT/pk/:更新一个用户信息
    DELETE/pk/:删除一个用户信息
    """
    queryset = Users_Conversation.objects.all()
    serializer_class = UsersConversationModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class SalesLoginView(APIView):
    """
    内部销售代表人员
    GET：得到所有销售代表信息
    POST：添加销售代表信息
    """
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        job = request.data.get('job')
        sale_login = sales.objects.filter(account=account).first()

        if sale_login and check_password(password, sale_login.password) and job == sale_login.job:
            return Response({
                'msg': '登录成功',
                'code': status.HTTP_200_OK,
                'user_id': sale_login.id,
                'user_name':sale_login.name,
                'sales_depart':sale_login.sales_depart.id
            })
        else:
            return Response({'msg': '登录失败', 'code': status.HTTP_400_BAD_REQUEST})


class SalesRegisterView(APIView):
    """
    注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        sales_depart = request.data.get('sales_depart')
        # print(make_password(password1))
        if sales.objects.filter(account=account):
            return Response({'msg': '该用户已注册！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                    'sales_depart': sales_depart,
                }
                sales_register_serializer = SaleLoginRegisterModelSerializer(data=user_data)
                if sales_register_serializer.is_valid():
                    sales_register_serializer.save()
                    return Response({'msg': '注册成功！', 'code': status.HTTP_200_OK})
                else:
                    return Response({'msg': sales_register_serializer.errors, 'code': status.HTTP_400_BAD_REQUEST})
            else:
                return Response({'msg': '两次密码不一致！', 'code': status.HTTP_400_BAD_REQUEST})

class SalesView(generics.ListCreateAPIView):
    """
    内部销售代表人员
    GET/pk/:得到一个销售代表信息
    PUT/pk/:更新一个销售代表信息
    DELETE/pk/:删除一个销售代表信息
    """
    queryset = sales.objects.all()
    serializer_class = SaleModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class DepartMangerLoginView(APIView):
    """
    部门经理登录功能
    """
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        job = request.data.get('job')

        DepartManger_login = DepartManger.objects.filter(account=account).first()
        print(DepartManger_login.sales_depart.id)
        sales_depart = DepartManger_login.sales_depart
        if DepartManger_login and check_password(password, DepartManger_login.password) and job == DepartManger_login.job:
            return Response({
                'msg': '登录成功',
                'code': status.HTTP_200_OK,
                'user_id': DepartManger_login.id,
                'user_name': DepartManger_login.name,
                'sales_depart': DepartManger_login.sales_depart.id
            })
        else:
            return Response({'msg': '登录失败', 'code': status.HTTP_400_BAD_REQUEST})

class DepartMangerRegisterView(APIView):
    """
    部门经理注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        sales_depart = request.data.get('sales_depart')
        # print(make_password(password1))
        if DepartManger.objects.filter(sales_depart=sales_depart):
            return Response({'msg': '该部门已经注册部门经理！', 'code': status.HTTP_400_BAD_REQUEST})
        elif DepartManger.objects.filter(account=account):
            return Response({'msg': '该用户已注册！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                    'sales_depart': sales_depart,
                }
                DepartManger_register_serializer = DepartMangerLoginRegisterModelSerializer(data=user_data)
                if DepartManger_register_serializer.is_valid():
                    DepartManger_register_serializer.save()
                    return Response({'msg': '注册成功！', 'code': status.HTTP_200_OK})
                else:
                    return Response({'msg': DepartManger_register_serializer.errors, 'code': status.HTTP_400_BAD_REQUEST})
            else:
                return Response({'msg': '两次密码不一致！', 'code': status.HTTP_400_BAD_REQUEST})

class DepartMangerView(generics.ListCreateAPIView):
    """
    部门经理
    GET/:得到所有部门经理信息
    POST/:添加部门经理信息
    """
    queryset = DepartManger.objects.all()
    serializer_class = DepartModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class DepartMangerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    部门经理
    GET/pk/:得到一个部门经理信息
    PUT/pk/:更新一个部门经理信息
    DELETE/pk/:删除一个部门经理信息
    """
    queryset = DepartManger.objects.all()
    serializer_class = DepartModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class SalesDirectorLoginView(APIView):
    """
    销售总监登录
    """
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        job = request.data.get('job')

        SalesDirector_login = SalesDirector.objects.filter(account=account).first()

        if SalesDirector_login and check_password(password, SalesDirector_login.password) and job == SalesDirector_login.job:
            return Response({
                'msg': '登录成功',
                'code': status.HTTP_200_OK,
                'user_id': SalesDirector_login.id,
                'user_name': SalesDirector_login.name,
                'war_zone':SalesDirector_login.war_zone.id
            })
        else:
            return Response({'msg': '登录失败', 'code': status.HTTP_400_BAD_REQUEST})

class SalesDirectorRegisterView(APIView):
    """
    销售总监注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        war_zone = request.data.get('war_zone')
        # print(make_password(password1))
        if SalesDirector.objects.filter(war_zone=war_zone):
            return Response({'msg': '该战区已注册销售总监！', 'code': status.HTTP_400_BAD_REQUEST})
        elif SalesDirector.objects.filter(account=account):
            return Response({'msg': '账号已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                    'war_zone': war_zone,
                }
                SalesDirector_register_serializer = SalesDirectoLoginRegisterModelSerializer(data=user_data)
                if SalesDirector_register_serializer.is_valid():
                    SalesDirector_register_serializer.save()
                    return Response({'msg': '注册成功！', 'code': status.HTTP_200_OK})
                else:
                    return Response({'msg': SalesDirector_register_serializer.errors, 'code': status.HTTP_400_BAD_REQUEST})
            else:
                return Response({'msg': '两次密码不一致！', 'code': status.HTTP_400_BAD_REQUEST})


class SalesDirectorView(generics.ListCreateAPIView):
    """
    销售总监
    GET/:得到所有销售总监信息
    POST/:添加销售总监信息
    """
    queryset = SalesDirector.objects.all()
    serializer_class = SalesDirectorModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class SalesDirectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    销售总监
    GET/pk/:得到一个销售总监信息
    PUT/pk/:更新一个销售总监信息
    DELETE/pk/:删除一个销售总监信息
    """
    queryset = SalesDirector.objects.all()
    serializer_class = SalesDirectorModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class SalesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    内部销售代表人员
    GET/pk/:得到一个销售代表信息
    PUT/pk/:更新一个销售代表信息
    DELETE/pk/:删除一个销售代表信息
    """
    queryset = sales.objects.all()
    serializer_class = SaleModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class WarZoneView(generics.ListCreateAPIView):
    """
    战区
    GET：得到所有战区信息
    POST：添加战区信息
    """
    queryset = War_Zone.objects.all()
    serializer_class = WarZoneModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能


class WarZoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    战区
    GET/pk/:得到一个战区信息
    PUT/pk/:更新一个战区信息
    DELETE/pk/:删除一个战区信息
    """
    queryset = War_Zone.objects.all()
    serializer_class = WarZoneModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class SalesDepartView(generics.ListCreateAPIView):
    """
    销售部
    GET：得到所有销售部信息
    POST：添加销售部信息
    """
    queryset = Sales_Depart.objects.all()
    serializer_class = SalesDepartModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能

class SaleDepartByWarZoneView(generics.ListCreateAPIView,APIView):
    """
    工作日志
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据用户id过滤
        前端需要传入一个销售人员ID
        """
        # 从URL获取sales_name参数
        war_zone = self.request.GET.get('war_zone')
        # print(sales_name)
        return Sales_Depart.objects.filter(war_zone=war_zone)

    queryset = Sales_Depart.objects.all()
    serializer_class = SalesDepartModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能


class SaleDepartDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    战区
    GET/pk/:得到一个销售部信息
    PUT/pk/:更新一个销售部信息
    DELETE/pk/:删除一个销售部信息
    """
    queryset = Sales_Depart.objects.all()
    serializer_class = SalesDepartModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class AdminLoginView(APIView):
    """
    系统管理员登录
    """
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        job = request.data.get('job')

        Admin_login = Admin.objects.filter(account=account).first()

        if Admin_login and check_password(password, Admin_login.password) and job == Admin_login.job:
            return Response({'msg': '登录成功', 'code': status.HTTP_200_OK, 'user_id': Admin_login.id,'user_name':Admin_login.name})
        else:
            return Response({'msg': '登录失败', 'code': status.HTTP_400_BAD_REQUEST})

class AdminRegisterView(APIView):
    """
    系统管理员注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        # print(make_password(password1))
        if Admin.objects.filter(account=account):
            return Response({'msg': '账号已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                }
                Admin_register_serializer = AdminLoginRegisterModelSerializer(data=user_data)
                if Admin_register_serializer.is_valid():
                    Admin_register_serializer.save()
                    return Response({'msg': '注册成功！', 'code': status.HTTP_200_OK})
                else:
                    return Response({'msg': Admin_register_serializer.errors, 'code': status.HTTP_400_BAD_REQUEST})
            else:
                return Response({'msg': '两次密码不一致！', 'code': status.HTTP_400_BAD_REQUEST})

class AdminView(generics.ListCreateAPIView):
    """
    系统管理员
    GET：得到所有系统管理员信息
    POST：添加系统管理员信息
    """
    queryset = Admin.objects.all()
    serializer_class = AdminModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能


class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    系统管理员
    GET/pk/:得到一个系统管理员信息
    PUT/pk/:更新一个系统管理员信息
    DELETE/pk/:删除一个系统管理员信息
    """
    queryset = Admin.objects.all()
    serializer_class = AdminModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class GeneralMangerLoginView(APIView):
    """
    总经理登录
    """
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        job = request.data.get('job')

        General_Manager_login = General_Manager.objects.filter(account=account).first()

        if General_Manager_login and check_password(password, General_Manager_login.password) and job == General_Manager_login.job:
            return Response({'msg': '登录成功', 'code': status.HTTP_200_OK, 'user_id': General_Manager_login.id,'user_name':General_Manager_login.name})
        else:
            return Response({'msg': '登录失败', 'code': status.HTTP_400_BAD_REQUEST})

class GeneralMangerRegisterView(APIView):
    """
    总经理注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        # print(make_password(password1))
        if Admin.objects.filter(account=account):
            return Response({'msg': '账号已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                }
                General_Manager_serializer = GeneralManagerRegisterModelSerializer(data=user_data)
                if General_Manager_serializer.is_valid():
                    General_Manager_serializer.save()
                    return Response({'msg': '注册成功！', 'code': status.HTTP_200_OK})
                else:
                    return Response({'msg': General_Manager_serializer.errors, 'code': status.HTTP_400_BAD_REQUEST})
            else:
                return Response({'msg': '两次密码不一致！', 'code': status.HTTP_400_BAD_REQUEST})

class GeneralMangerView(generics.ListCreateAPIView):
    """
    总经理
    GET：得到所有总经理信息
    POST：添加总经理信息
    """
    queryset = General_Manager.objects.all()
    serializer_class = GeneralManagerModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能


class GeneralMangerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    总经理
    GET/pk/:得到一个总经理信息
    PUT/pk/:更新一个总经理信息
    DELETE/pk/:删除一个总经理信息
    """
    queryset = General_Manager.objects.all()
    serializer_class = GeneralManagerModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class JobLogView(generics.ListCreateAPIView,APIView):
    """
    工作日志
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据用户id过滤
        前端需要传入一个销售人员ID
        """
        # 从URL获取sales_name参数
        sales_name = self.request.GET.get('sales_name')
        # print(sales_name)
        return Job_Log.objects.filter(sales_name=sales_name)

    queryset = Job_Log.objects.all()
    serializer_class = JobLogModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能

class JobLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    工作日志
    GET/pk/:得到一个工作日志信息
    PUT/pk/:更新一个工作日志信息
    DELETE/pk/:删除一个工作日志信息
    """
    queryset = Job_Log.objects.all()
    serializer_class = JobLogModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能


class EffictvieUsersBySalesView(generics.ListAPIView,APIView):
    """
    销售代表记录的有效客户数
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据用户id过滤
        前端需要传入一个销售人员ID
        """
        # 从URL获取sales_name参数
        sales_name = self.request.GET.get('sales_name')
        # 根据审核状态字段跟新status字段
        Effictive_Users.objects.filter(check_status=True).update(order_status="贷款已下放")
        Effictive_Users.objects.filter(check_status=False).update(order_status="订单审核中")

        querysets = Effictive_Users.objects.all()
        for queryset in querysets:
            print(queryset.contract_amount)
            count = service_fee(queryset.contract_amount)
            Effictive_Users.objects.filter(id=queryset.id).update(service_fee_number=count)

        return Effictive_Users.objects.filter(sales_name=sales_name)
    serializer_class = EffictiveUsersModelSerializer
    pagination_class = UserPageNumberPagination  # 局部分页
    filter_backends = [NameSearchFilter]  # 查询功能

    def post(self,request):
        name = request.data.get('name')
        age = request.data.get('age')
        sex = request.data.get('sex')
        telephone = request.data.get('telephone')
        job = request.data.get('job')
        create_time = request.data.get('create_time')
        order_status = request.data.get('order_status')
        contract_amount = request.data.get('contract_amount')
        loan_amount = request.data.get('loan_amount')
        sales_name = request.data.get('sales_name')
        img_id_card = request.FILES.get('img_id_card')
        check_status = request.data.get('check_status')
        contract_number =request.data.get('contract_number')
        service_fee_number = service_fee(contract_number)
        service_fee_status = request.data.get('service_fee_status')
        note = request.data.get('note')
        if Effictive_Users.objects.filter(telephone=telephone):
            return Response({'msg': '该用户已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            user_data = {
                'name': name,
                'age': age,
                'sex': sex,
                'telephone': telephone,
                'sales_name': sales_name,
                'create_time': create_time,
                'order_status':order_status,
                'loan_amount': loan_amount,
                'contract_amount': contract_amount,
                'img_id_card': img_id_card,
                'contract_number':contract_number,
                'check_status':check_status,
                'service_fee_number':service_fee_number,
                'service_fee_status':service_fee_status,
                'note':note,
                'job':job
            }
            Effictive_Users_serializer = EffictiveUsersModelSerializer(data=user_data)
            if Effictive_Users_serializer.is_valid():
                Effictive_Users_serializer.save()
                return Response({'msg': '注册成功！', 'code': status.HTTP_200_OK})
            else:
                return Response({'msg': Effictive_Users_serializer.errors, 'code': status.HTTP_400_BAD_REQUEST})


class EffictvieUsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    销售代表有效用户
    """
    queryset = Effictive_Users.objects.all()
    serializer_class = EffictiveUsersModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class EffictvieUsersView(generics.ListCreateAPIView):
    """
    销售代表有效用户
    """
    queryset = Effictive_Users.objects.all()
    serializer_class = EffictiveUsersModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class EffictvieUsersByDepartMangerView(generics.ListAPIView,APIView):
    """
    销售代表记录的有效客户数
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据部门ID过滤
        前端需要传入一个部门ID
        """
        Effictive_Users.objects.filter(check_status=True).update(order_status="贷款已下放")
        Effictive_Users.objects.filter(check_status=False).update(order_status="订单审核中")

        querysets = Effictive_Users.objects.all()
        for queryset in querysets:
            count = service_fee(queryset.contract_amount)
            Effictive_Users.objects.filter(id=queryset.id).update(service_fee_number=count)

        sales_depart = self.request.GET.get('sales_depart')
        # sales_depart = self.request.data.get('sales_depart')
        sales_people = sales.objects.filter(sales_depart=sales_depart)
        if len(sales_people) >= 2:
            # 初始化空的queryset，用于后续循环合并
            queryset = Effictive_Users.objects.none()
            for sale_people in sales_people:
                queryset = queryset | Effictive_Users.objects.filter(sales_name=sale_people.id)
            return queryset
        else:
            return Effictive_Users.objects.filter(sales_name=sales_people.id)

    queryset = Effictive_Users.objects.all()
    serializer_class = EffictiveUsersModelSerializer
    pagination_class = UserPageNumberPagination  # 局部分页
    filter_backends = [NameSearchFilter]  # 查询功能

class EffictvieUsersBySalesDirectorView(generics.ListAPIView,APIView):
    """
    销售代表记录的有效客户数
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据战区ID过滤
        前端需要传入一个战区ID
        """
        Effictive_Users.objects.filter(check_status=True).update(status="贷款已下放")
        Effictive_Users.objects.filter(check_status=False).update(status="订单审核中")

        querysets = Effictive_Users.objects.all()
        for queryset in querysets:
            count = service_fee(queryset.contract_amount)
            Effictive_Users.objects.filter(id=queryset.id).update(service_fee_number=count)

        war_zone = self.request.GET.get('war_zone')
        # 根据战区查找该战区下的销售部门
        sales_departs = Sales_Depart.objects.filter(war_zone=war_zone)
        salesquerysets = sales.objects.none()
        # 循环遍历所有销售部门下的销售代表
        for sales_depart in sales_departs:
            salesquerysets = salesquerysets | sales.objects.filter(sales_depart=sales_depart.id)
        queryset = Effictive_Users.objects.none()
        # 根据销售代表循环遍历销售代表下的客户
        for sale_people in salesquerysets:
            queryset = queryset | Effictive_Users.objects.filter(sales_name=sale_people.id)
        return queryset

    queryset = Effictive_Users.objects.all()
    serializer_class = EffictiveUsersModelSerializer
    pagination_class = UserPageNumberPagination  # 局部分页
    filter_backends = [NameSearchFilter]  # 查询功能

class EffictvieUsersHistoryView(generics.ListAPIView,APIView):
    """
    销售代表记录的有效客户数
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据战区ID过滤
        前端需要传入一个战区ID
        """
        Effictive_Users.objects.filter(check_status=True).update(order_status="贷款已下放")
        Effictive_Users.objects.filter(check_status=False).update(order_status="订单审核中")

        querysets = Effictive_Users.objects.all()
        for queryset in querysets:
            count = service_fee(queryset.contract_amount)
            Effictive_Users.objects.filter(id=queryset.id).update(service_fee_number=count)
        return Effictive_Users.objects.filter(check_status=True)

    queryset = Effictive_Users.objects.all()
    serializer_class = EffictiveUsersModelSerializer
    pagination_class = UserPageNumberPagination  # 局部分页
    filter_backends = [NameSearchFilter]  # 查询功能

class EffictvieUsersNoFeeView(generics.ListAPIView,APIView):
    """
    销售代表记录的有效客户数
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据战区ID过滤
        前端需要传入一个战区ID
        """
        Effictive_Users.objects.filter(check_status=True).update(order_status="贷款已下放")
        Effictive_Users.objects.filter(check_status=False).update(order_status="订单审核中")

        querysets = Effictive_Users.objects.all()
        for queryset in querysets:
            count = service_fee(queryset.contract_amount)
            Effictive_Users.objects.filter(id=queryset.id).update(service_fee_number=count)
        return Effictive_Users.objects.filter(check_status=False)

    queryset = Effictive_Users.objects.all()
    serializer_class = EffictiveUsersModelSerializer
    pagination_class = UserPageNumberPagination  # 局部分页
    filter_backends = [NameSearchFilter]  # 查询功能

class EffictvieUsersUpdateFeeView(generics.ListAPIView,APIView):
    """
    销售代表记录的有效客户数
    """
    def post(self,request):
        """
        重写get_queryset方法
        根据战区ID过滤
        前端需要传入一个战区ID
        """
        Effictive_Users.objects.filter(check_status=True).update(order_status="贷款已下放")
        Effictive_Users.objects.filter(check_status=False).update(order_status="订单审核中")

        id = self.request.GET.get('id')
        fee = self.request.data.get('fee')
        check_status = request.data.get('check_status')
        Effictive_Users.objects.filter(id=id).update(service_fee_status=fee,check_status=check_status)
        querysets = Effictive_Users.objects.all()
        for queryset in querysets:
            count = service_fee(queryset.contract_amount)
            Effictive_Users.objects.filter(id=queryset.id).update(service_fee_number=count)
        return Response({'msg': '更新成功！', 'code': status.HTTP_200_OK})
        # return Effictive_Users.objects.filter(check_status=False)

    queryset = Effictive_Users.objects.all()
    serializer_class = EffictiveUsersModelSerializer
    pagination_class = UserPageNumberPagination  # 局部分页
    filter_backends = [NameSearchFilter]  # 查询功能

class EffictvieUsersFeeView(generics.ListAPIView,APIView):
    """
    销售代表记录的有效客户数
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据战区ID过滤
        前端需要传入一个战区ID
        """
        Effictive_Users.objects.filter(check_status=True).update(order_status="贷款已下放")
        Effictive_Users.objects.filter(check_status=False).update(order_status="订单审核中")

        querysets = Effictive_Users.objects.all()
        for queryset in querysets:
            count = service_fee(queryset.contract_amount)
            Effictive_Users.objects.filter(id=queryset.id).update(service_fee_number=count)
        return Effictive_Users.objects.filter(check_status=True)

    queryset = Effictive_Users.objects.all()
    serializer_class = EffictiveUsersModelSerializer
    pagination_class = UserPageNumberPagination  # 局部分页
    filter_backends = [NameSearchFilter]  # 查询功能

class OpLogsMangerView(generics.ListAPIView):
    """
    操作日志
    """
    queryset = OpLogs.objects.all()
    serializer_class = OpLogsModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能

class FinancialCommissionLoginView(APIView):
    """
    金融专员登录
    """
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        job = request.data.get('job')

        Financial_Commissioner_login = Financial_Commissioner.objects.filter(account=account).first()

        if Financial_Commissioner_login and check_password(password, Financial_Commissioner_login.password) and job == Financial_Commissioner_login.job:
            return Response({'msg': '登录成功', 'code': status.HTTP_200_OK, 'user_id': Financial_Commissioner_login.id,'user_name':Financial_Commissioner_login.name})
        else:
            return Response({'msg': '登录失败', 'code': status.HTTP_400_BAD_REQUEST})

class FinancialCommissionRegisterView(APIView):
    """
    金融专员注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        if Financial_Commissioner.objects.filter(account=account):
            return Response({'msg': '账号已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                }
                Financial_Commissioner_register_serializer = FinancialCommissionModelSerializer(data=user_data)
                if Financial_Commissioner_register_serializer.is_valid():
                    Financial_Commissioner_register_serializer.save()
                    return Response({'msg': '注册成功！', 'code': status.HTTP_200_OK})
                else:
                    return Response({'msg': Financial_Commissioner_register_serializer.errors, 'code': status.HTTP_400_BAD_REQUEST})
            else:
                return Response({'msg': '两次密码不一致！', 'code': status.HTTP_400_BAD_REQUEST})

class FinancialCommissionView(generics.ListCreateAPIView):
    """
    金融专员
    GET：得到所有金融专员信息
    POST：添加金融专员信息
    """
    queryset = Financial_Commissioner.objects.all()
    serializer_class = FinancialCommissionModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能


class FinancialCommissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    金融专员
    GET/pk/:得到一个金融专员信息
    PUT/pk/:更新一个金融专员信息
    DELETE/pk/:删除一个金融专员信息
    """
    queryset = Financial_Commissioner.objects.all()
    serializer_class = FinancialCommissionModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class PerformanceByAll(generics.ListAPIView,APIView):
    """
    业绩展示(所有，金融部看)
    """
    """
    """
    def get(self,request):
        Performance_data=[]
        sales_people = sales.objects.all()
        for sale_people in sales_people:
            Performance_count = 0.0
            sale_performances = Effictive_Users.objects.filter(sales_name=sale_people.id)
            for sale_performance in sale_performances:
                contract_amount = float(sale_performance.contract_amount)
                Performance_count += contract_amount
            data = {
                'id':sale_people.id,
                'sale_name': sale_people.name,
                'contract_amount_total': Performance_count,
            }
            Performance_data.append(data)
        # print(Performance_data)
        return Response({'Performance_data':Performance_data,'code': status.HTTP_200_OK})

class PerformanceBySaleDepart(generics.ListAPIView,APIView):
    """
    业绩展示（一个部门下，部门经理看
    """
    """
    """
    def get(self,request):
        Performance_data=[]
        sales_depart = self.request.GET.get('sales_depart')
        sales_people = sales.objects.filter(sales_depart=sales_depart)
        for sale_people in sales_people:
            Performance_count = 0.0
            sale_performances = Effictive_Users.objects.filter(sales_name=sale_people.id)
            for sale_performance in sale_performances:
                contract_amount = float(sale_performance.contract_amount)
                Performance_count += contract_amount
            data = {
                'id':sale_people.id,
                'sale_name': sale_people.name,
                'contract_amount_total': Performance_count,
            }
            Performance_data.append(data)
        # print(Performance_data)
        return Response({'Performance_data':Performance_data,'code': status.HTTP_200_OK})

class PerformanceBySaleDirector(generics.ListAPIView,APIView):
    """
    业绩展示（战区，销售总监看
    """
    """
    """
    def get(self,request):
        Performance_data=[]
        war_zone = self.request.GET.get('war_zone')
        sales_departs = Sales_Depart.objects.filter(war_zone=war_zone)
        for sales_depart in sales_departs:
            sales_people = sales.objects.filter(sales_depart=sales_depart.id)
            for sale_people in sales_people:
                Performance_count = 0.0
                sale_performances = Effictive_Users.objects.filter(sales_name=sale_people.id)
                for sale_performance in sale_performances:
                    contract_amount = float(sale_performance.contract_amount)
                    Performance_count += contract_amount
                data = {
                    'id':sale_people.id,
                    'sale_name': sale_people.name,
                    'contract_amount_total': Performance_count,
                }
                Performance_data.append(data)
        # print(Performance_data)
        return Response({'Performance_data':Performance_data,'code': status.HTTP_200_OK})

class PerformanceBySale(generics.ListAPIView,APIView):
    """
    业绩展示（自己看，部门经理看
    """
    """
    """
    def get(self,request):
        Performance_data=[]
        Performance_count = 0
        sales_name = self.request.GET.get('sales_name')
        sale_performances = Effictive_Users.objects.filter(sales_name=sales_name)
        for sale_performance in sale_performances:
            contract_amount = float(sale_performance.contract_amount)
            Performance_count += contract_amount
        sales_peoples = sales.objects.filter(id=sales_name)
        for sales_people in sales_peoples:
            print(sales_people.name)
        data = {
            'id':sales_name,
            'sale_name': sales_people.name,
            'contract_amount_total': Performance_count,
        }
        Performance_data.append(data)
        return Response({'Performance_data':Performance_data,'code': status.HTTP_200_OK})

class SalesBySaleDepartView(generics.ListCreateAPIView,APIView):
    """
    根据部门ID获取该部门下所有的销售代表
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据用户id过滤
        前端需要传入一个销售人员ID
        """
        # 从URL获取sales_name参数
        sales_depart = self.request.GET.get('sales_depart')
        # print(sales_name)
        return sales.objects.filter(sales_depart=sales_depart)

    # queryset = sales.objects.all()
    serializer_class = SaleModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能

class SalesByWarZoneView(generics.ListCreateAPIView,APIView):
    """
    根据战区ID获取该战区下所有的部门经理
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据用户id过滤
        前端需要传入一个销售人员ID
        """
        war_zone = self.request.GET.get('war_zone')
        sales_departs = Sales_Depart.objects.filter(war_zone=war_zone)
        departmangerquerysets = DepartManger.objects.none()
        for sales_deaprt in sales_departs:
            departmangerquerysets = departmangerquerysets | DepartManger.objects.filter(sales_depart=sales_deaprt.id)
        return departmangerquerysets

    serializer_class = SaleModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能

class ContractByCustomerView(generics.ListAPIView,APIView):
    """
    销售代表记录的有效客户数
    """
    def get_queryset(self):
        """
        重写get_queryset方法
        根据用户id过滤
        前端需要传入一个销售人员ID
        """
        # 从URL获取sales_name参数
        contract_number = self.request.GET.get('contract_number')

        return Contract.objects.filter(contract_number=contract_number)
        # Effictive_Users.objects.filter(start_time__month=10)
    # queryset = Effictive_Users.objects.all()
    serializer_class = ContractModelSerializer
    pagination_class = UserPageNumberPagination  # 局部分页
    filter_backends = [NameSearchFilter]  # 查询功能

    def post(self,request):
        contract_name = request.data.get('contract_name')
        contract_number = request.data.get('contract_number')
        contract_time = request.data.get('contract_time')
        contract_money = request.data.get('contract_money')
        contract_image = request.FILES.get('contract_image')
        effictiveusers_id = request.data.get('effictiveusers_id')

        if Contract.objects.filter(contract_number=contract_number):
            return Response({'msg': '合同编号已存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            contract_data = {
                'contract_name': contract_name,
                'contract_number': contract_number,
                'contract_time': contract_time,
                'contract_money': contract_money,
                'contract_image': contract_image,
                'effictiveusers_id': effictiveusers_id
            }
            Contract_serializer = ContractModelSerializer(data=contract_data)
            if Contract_serializer.is_valid():
                Contract_serializer.save()
                return Response({'msg': '添加成功！', 'code': status.HTTP_200_OK})
            else:
                return Response({'msg': Contract_serializer.errors, 'code': status.HTTP_400_BAD_REQUEST})

class ContractView(generics.ListCreateAPIView):
    """
    合同详情
    """
    queryset = Contract.objects.all()
    serializer_class = ContractModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    合同详情
    """
    queryset = Contract.objects.all()
    serializer_class = ContractModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能

class AccountantLoginView(APIView):
    """
    会计登录
    """
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        job = request.data.get('job')

        Accountant_login = Accountant.objects.filter(account=account).first()

        if Accountant_login and check_password(password, Accountant_login.password) and job == Accountant_login.job:
            return Response({'msg': '登录成功', 'code': status.HTTP_200_OK, 'user_id': Accountant_login.id,'user_name':Accountant_login.name})
        else:
            return Response({'msg': '登录失败', 'code': status.HTTP_400_BAD_REQUEST})

class AccountantRegisterView(APIView):
    """
    总经理注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        if Accountant.objects.filter(account=account):
            return Response({'msg': '账号已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                }
                Accountant_serializer = AccountantModelSerializer(data=user_data)
                if Accountant_serializer.is_valid():
                    Accountant_serializer.save()
                    return Response({'msg': '注册成功！', 'code': status.HTTP_200_OK})
                else:
                    return Response({'msg': Accountant_serializer.errors, 'code': status.HTTP_400_BAD_REQUEST})
            else:
                return Response({'msg': '两次密码不一致！', 'code': status.HTTP_400_BAD_REQUEST})

class AdminUpdateView(APIView):
    """
    总经理注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        id = self.request.GET.get('id')
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        if Admin.objects.filter(account=account):
            return Response({'msg': '账号已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                }
                Admin.objects.filter(id=id).update(name=name,sex=sex,account=account,password=make_password(password1),create_time=create_time,job=job)
                return Response({'msg': '更新成功！', 'code': status.HTTP_200_OK})

class SalesUpdateView(APIView):
    """
    总经理注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        id = self.request.GET.get('id')
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        sales_depart = request.data.get('sales_depart')
        if sales.objects.filter(account=account):
            return Response({'msg': '账号已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                    'sales_depart':sales_depart,
                }
                sales.objects.filter(id=id).update(name=name,sex=sex,account=account,password=make_password(password1),create_time=create_time,job=job,sales_depart=sales_depart)
                return Response({'msg': '更新成功！', 'code': status.HTTP_200_OK})

class FinancialUpdateView(APIView):
    """
    总经理注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        id = self.request.GET.get('id')
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        # sales_depart = request.data.get('sales_depart')
        if Financial_Commissioner.objects.filter(account=account):
            return Response({'msg': '账号已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                    # 'sales_depart':sales_depart,
                }
                Financial_Commissioner.objects.filter(id=id).update(name=name,sex=sex,account=account,password=make_password(password1),create_time=create_time,job=job)
                return Response({'msg': '更新成功！', 'code': status.HTTP_200_OK})

class GeneralMangerUpdateView(APIView):
    """
    总经理注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        id = self.request.GET.get('id')
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        if General_Manager.objects.filter(account=account):
            return Response({'msg': '账号已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                }
                General_Manager.objects.filter(id=id).update(name=name,sex=sex,account=account,password=make_password(password1),create_time=create_time,job=job)
                return Response({'msg': '更新成功！', 'code': status.HTTP_200_OK})

class AccountantUpdateView(APIView):
    """
    总经理注册功能
    获取表单数据：
    account 账号
    password1 密码
    password2 确认密码
    sex 性别
    job 职位
    create_time 入职时间
    name 姓名
    """
    def post(self, request):
        id = self.request.GET.get('id')
        name = request.data.get('name')
        sex = request.data.get('sex')
        account = request.data.get('account')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        create_time = request.data.get('create_time')
        job = request.data.get('job')
        if Accountant.objects.filter(account=account):
            return Response({'msg': '账号已经存在！', 'code': status.HTTP_400_BAD_REQUEST})
        else:
            if password1 == password2:
                user_data = {
                    'name': name,
                    'sex': sex,
                    'account': account,
                    'password': make_password(password1),
                    'create_time': create_time,
                    'job': job,
                }
                Accountant.objects.filter(id=id).update(name=name,sex=sex,account=account,password=make_password(password1),create_time=create_time,job=job)
                return Response({'msg': '更新成功！', 'code': status.HTTP_200_OK})

class AccountantView(generics.ListCreateAPIView):
    """
    系统管理员
    GET：得到所有系统管理员信息
    POST：添加系统管理员信息
    """
    queryset = Accountant.objects.all()
    serializer_class = AccountantModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] #查询功能


class AccountantDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    系统管理员
    GET/pk/:得到一个系统管理员信息
    PUT/pk/:更新一个系统管理员信息
    DELETE/pk/:删除一个系统管理员信息
    """
    queryset = Accountant.objects.all()
    serializer_class = AccountantModelSerializer
    pagination_class = UserPageNumberPagination # 局部分页
    filter_backends = [NameSearchFilter] # 查询功能