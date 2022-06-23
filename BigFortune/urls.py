"""BigFortune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from Users.views import EffictvieUsersDetailView

schema_view = get_schema_view(
    openapi.Info(
        title="大富翁金融系统接口文档", #必传 文档名字
        default_version='v1.0.0' # 必传 文档版本
    ),
    public=True, # 所有人可访问
    # permission_classes=(IsAuthenticated,) # 控制权限访问
)

router = DefaultRouter()
router.register(r'Imgupload',EffictvieUsersDetailView , basename='pic')

urlpatterns = [
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
    path('admin/', admin.site.urls),
    path('users/', include('Users.urls')),
    # 注意是 media 而不是 upload
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
