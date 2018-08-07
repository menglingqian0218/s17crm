import re
from django.shortcuts import redirect,HttpResponse
from django.conf import settings

class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

class RbacMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # 1. 当前请求URL
        current_request_url = request.path_info

        # 2. 处理白名单
        for url in settings.VALID_URL_LIST:
            if re.match(url,current_request_url):
                return None

        # 3. 获取session中保存的权限信息
        permission_dict = request.session.get(settings.XX)
        if not permission_dict:
            return redirect(settings.RBAC_LOGIN_URL)

        flag = False
        for group_id, values in permission_dict.items():
            for url in values['urls']:
                regex = settings.URL_FORMAT.format(url)
                if re.match(regex, current_request_url):
                    flag = True
                    break
            if flag:
                break

        if not flag:
            return HttpResponse('无权访问')