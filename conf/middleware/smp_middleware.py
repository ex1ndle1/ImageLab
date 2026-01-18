from django.http import HttpResponse
from django.shortcuts import redirect
class CheckIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):


        # if request.META.get('REMOTE_ADDR') :
        #         print(f'''ip:{request.META.get('REMOTE_ADDR')}''')
        
        
    
        # print(request)     
        # print(request.session.get('_auth_user_id'))
        response = self.get_response(request)
        return response
        

        