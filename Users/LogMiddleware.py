import time
import json
from django.utils.deprecation import MiddlewareMixin
import urllib.parse
# 获取日志logger
import logging
from Users.models import OpLogs, AccessTimeOutLogs

logger = logging.getLogger(__name__)


class LogMiddle(MiddlewareMixin):
    # 日志处理中间件
    def __init__(self, *args):
        super(LogMiddle, self).__init__(*args)

        self.start_time = None  # 开始时间
        self.end_time = None  # 响应时间
        self.data = {}  # dict数据

    def process_request(self, request):
        # 存放请求过来时的时间
        request.init_time = time.time()
        self.start_time = time.time()  # 开始时间
        re_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 请求时间（北京）
        # 请求IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # 如果有代理，获取真实IP
            re_ip = x_forwarded_for.split(",")[0]
        else:
            re_ip = request.META.get('REMOTE_ADDR')
        # 请求方法
        re_method = request.method
        print(re_method)
        # 请求参数
        re_content = request.GET if re_method == 'GET' else request.POST
        if re_content:
            # 筛选空参数
            re_content = json.dumps(re_content)
        else:
            re_content = None
        self.data.update(
            {
                're_time': re_time,  # 请求时间
                're_url': request.path,  # 请求url
                're_method': re_method,  # 请求方法
                're_ip': re_ip,  # 请求IP
                're_content': re_content,  # 请求参数
                # 're_user': request.user.username    # 操作人(需修改)，网站登录用户
                # 're_user': 'AnonymousUser'  # 匿名操作用户测试
            }
        )
        # OpLogs.objects.create(**self.data)
        # print(self.data)
        return None

    def process_response(self, request, response):
        try:
			# 耗时
            localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # 请求路径
            path = request.path
            # 请求方式
            method = request.method
            # 响应状态码
            status_code = response.status_code
            # 响应内容
            content = response.content
            # 记录信息
            content = str(content.decode('utf-8'))
            content = urllib.parse.unquote(content)
            content = (json.loads(content))
            message = '%s %s %s %s %s' % (localtime, path, method, status_code, content)
            self.data['rp_content'] = content
            # 耗时
            self.end_time = time.time()  # 响应时间
            access_time = self.end_time - self.start_time
            self.data['access_time'] = round(access_time * 1000)  # 耗时毫秒/ms
            if self.data.get('access_time') > 3 * 1000:
                AccessTimeOutLogs.objects.create(**self.data)  # 超时操作日志入库db
            OpLogs.objects.create(**self.data)  # 操作日志入库db
            logger.info(message)
        except:
            logger.critical('系统错误')
        return response
