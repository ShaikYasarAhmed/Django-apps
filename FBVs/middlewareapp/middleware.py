from django.http import HttpResponse
class ExecutionFLowMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('this line added at pre-processing of request')
        response=self.get_response(request)
        print('this line added at post-processing of request')
        return response
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
      self.get_response=get_response
    def __call__(self,request):
      #response=self.get_response(request)
      return HttpResponse('Currently Application under maintenance... plz try after 2 days!!!')
class ErrorMessageMiddleware(object):
   def __init__(self,get_response):
     self.get_response=get_response

   def __call__(self,request):
      return self.get_response(request)

   def process_exception(self,request,exception):
      return HttpResponse('<h1>Currently we are facing some technical problems plz try after some time!!!</h1>')
class Firstmiddleware(object):
    def __init__(self,get_response):
      self.get_response=get_response

    def __call__(self,request):
      print('This line printed by first middleware at preprocessing of request')
      response=self.get_response(request)
      print('This line printed by first middleware at post-processing of request')
      return response
class Secondmiddleware(object):
    def __init__(self,get_response):
      self.get_response=get_response

    def __call__(self,request):
      print('This line printed by second middleware at preprocessing of request')
      response=self.get_response(request)
      print('This line printed by second middleware at post-processing of request')
      return response
