from django.urls import path, re_path

from Users.views import UserView,UserDetailView
# from Users.views import EmployeeRegisterView,EmploymeeLoginView
from Users.views import UserConversationDetailView, UserConversationView
from Users.views import SalesLoginView, SalesDetailView, SalesRegisterView, SalesView
from Users.views import SaleDepartDetailView, SalesDepartView
from Users.views import WarZoneView, WarZoneDetailView
from Users.views import DepartMangerLoginView,DepartMangerRegisterView,DepartMangerView,DepartMangerDetailView
from Users.views import SalesDirectorDetailView,SalesDirectorLoginView,SalesDirectorRegisterView,SalesDirectorView
from Users.views import AdminLoginView,AdminRegisterView,AdminDetailView,AdminView
from Users.views import GeneralMangerView,GeneralMangerDetailView,GeneralMangerLoginView,GeneralMangerRegisterView
from Users.views import JobLogView,JobLogDetailView
from Users.views import EffictvieUsersBySalesView,EffictvieUsersDetailView,EffictvieUsersByDepartMangerView, EffictvieUsersBySalesDirectorView
from Users.views import UserConversationView,UserConversationDetailView
from Users.views import OpLogsMangerView
from Users.views import FinancialCommissionDetailView,FinancialCommissionLoginView,FinancialCommissionRegisterView,FinancialCommissionView
from Users.views import PerformanceByAll,SalesBySaleDepartView,SalesByWarZoneView,PerformanceBySaleDepart
from Users.views import PerformanceBySaleDirector,ContractView,ContractDetailView
from Users.views import Accountant,AccountantLoginView,AccountantRegisterView
from Users.views import AccountantView,AccountantDetailView,EffictvieUsersView,SaleDepartByWarZoneView
from Users.views import EffictvieUsersHistoryView,EffictvieUsersNoFeeView
from Users.views import PerformanceBySale,AccountantUpdateView,AdminUpdateView,GeneralMangerUpdateView,ContractByCustomerView
from Users.views import EffictvieUsersFeeView,EffictvieUsersUpdateFeeView,SalesUpdateView,FinancialUpdateView

urlpatterns = [
    # 公海库路由
    path('userinfo/', UserView.as_view()),
    re_path('^userinfo/(?P<pk>\d+)/$', UserDetailView.as_view()),

    # # 公司员工路由
    # path('employee/register/', EmployeeRegisterView.as_view()),
    # path('employee/login/', EmploymeeLoginView.as_view()),

    # re_path('^userinfo/(?P<pk>\d+)/$', UserDetailView.as_view()),

    # 内部销售代表路由
    path('sales/login/', SalesLoginView.as_view()),
    path('sales/register/', SalesRegisterView.as_view()),
    path('sales/update/', SalesUpdateView.as_view()),
    path('sales/', SalesView.as_view()),
    re_path('^sales/(?P<pk>\d+)/$', SalesDetailView.as_view()),

    # 内部部门经理路由
    path('departmanger/login/', DepartMangerLoginView.as_view()),
    path('departmanger/register/', DepartMangerRegisterView.as_view()),
    path('departmanger/', DepartMangerView.as_view()),
    re_path('^departmanger/(?P<pk>\d+)/$', DepartMangerDetailView.as_view()),

    # 内部销售总监路由
    path('salesdirector/login/', SalesDirectorLoginView.as_view()),
    path('salesdirector/register/', SalesDirectorRegisterView.as_view()),

    path('salesdirector/', SalesDirectorView.as_view()),
    re_path('^salesdirector/(?P<pk>\d+)/$', SalesDirectorDetailView.as_view()),

    # 战区路由
    path('warzone/', WarZoneView.as_view()),
    re_path('^warzone/(?P<pk>\d+)/$', WarZoneDetailView.as_view()),

    # 销售部门路由
    path('salesdepart/', SalesDepartView.as_view()),
    re_path('^salesdepart/(?P<pk>\d+)/$', SaleDepartDetailView.as_view()),

    # 系统管理员路由
    path('admin/login/', AdminLoginView.as_view()),
    path('admin/register/', AdminRegisterView.as_view()),
    path('admin/update/', AdminUpdateView.as_view()),
    path('admin/', AdminView.as_view()),
    re_path('^admin/(?P<pk>\d+)/$', AdminDetailView.as_view()),

    # 总经理路由
    path('generalmanager/login/', GeneralMangerLoginView.as_view()),
    path('generalmanager/register/', GeneralMangerRegisterView.as_view()),
    path('generalmanager/update/', GeneralMangerUpdateView.as_view()),
    path('generalmanager/', GeneralMangerView.as_view()),
    re_path('^generalmanager/(?P<pk>\d+)/$', GeneralMangerDetailView.as_view()),

    # 工作日志路由
    path('joblog/', JobLogView.as_view()),
    re_path('^joblog/(?P<pk>\d+)/$', JobLogDetailView.as_view()),

    # 销售代表记录客户路由
    path('effictiveusersbysales/', EffictvieUsersBySalesView.as_view()),
    path('effictiveusershistory/', EffictvieUsersHistoryView.as_view()),
    path('effictiveusersnofee/', EffictvieUsersNoFeeView.as_view()),
    path('effictiveusersupdatefee/', EffictvieUsersUpdateFeeView.as_view()),
    path('effictiveusersfee/', EffictvieUsersFeeView.as_view()),
    path('effictiveusersbyall/', EffictvieUsersView.as_view()),
    path('effictiveusersbydepartmanger/', EffictvieUsersByDepartMangerView.as_view()),
    path('effictiveusersbysalesdirector/', EffictvieUsersBySalesDirectorView.as_view()),
    re_path('^effictiveusers/(?P<pk>\d+)/$', EffictvieUsersDetailView.as_view()),

    #洽谈记录路由
    path('userconversation/', UserConversationView.as_view()),
    re_path('^userconversation/(?P<pk>\d+)/$', UserConversationDetailView.as_view()),

    # 操作日志
    path('oplogs/', OpLogsMangerView.as_view()),

    # 金融专员路由
    path('financialcommission/login/', FinancialCommissionLoginView.as_view()),
    path('financialcommission/register/', FinancialCommissionRegisterView.as_view()),
    path('financialcommission/update/', FinancialUpdateView.as_view()),
    path('financialcommission/', FinancialCommissionView.as_view()),
    re_path('^financialcommission/(?P<pk>\d+)/$', FinancialCommissionDetailView.as_view()),

    # 业绩
    path('performancebyall/', PerformanceByAll.as_view()),
    path('performancebysaledepart/', PerformanceBySaleDepart.as_view()),
    path('performancebysaledirector/', PerformanceBySaleDirector.as_view()),
    path('performancebysale/', PerformanceBySale.as_view()),

    # 根据部门ID获取销售代表
    path('salebysaledepart/', SalesBySaleDepartView.as_view()),

    # 根据战区ID获取部门经理
    path('salesbywarzone/', SalesByWarZoneView.as_view()),

    # 合同
    path('contract/', ContractView.as_view()),
    path('contractbyeffictusers/', ContractByCustomerView.as_view()),
    re_path('^contract/(?P<pk>\d+)/$', ContractDetailView.as_view()),

    # 会计
    path('accountant/login/', AccountantLoginView.as_view()),
    path('accountant/register/', AccountantRegisterView.as_view()),
    path('accountant/update/', AccountantUpdateView.as_view()),
    path('accountant/', AccountantView.as_view()),
    re_path('^accountant/(?P<pk>\d+)/$', AccountantDetailView.as_view()),

    # 根据战区ID得到部门
    path('salesdepartbywarzone/', SaleDepartByWarZoneView.as_view()),

]