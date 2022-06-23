from rest_framework.pagination import PageNumberPagination

class UserPageNumberPagination(PageNumberPagination):
    page_query_param = "page" # 查询字符串中代表页码的变量名
    page_size_query_param = "size" # 查询字符串中代表每一页数据的变量名
    page_size = 5 # 每一页的数据量
    max_page_size = 50 # 允许客户端通过查询字符串调整的最大单页数据量