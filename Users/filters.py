from rest_framework.filters import SearchFilter

class NameSearchFilter(SearchFilter):
    search_param = 'name' #查询关键字

    def get_search_fields(self, view, request):
        # 数据表中需要查询字段
        return ['name']