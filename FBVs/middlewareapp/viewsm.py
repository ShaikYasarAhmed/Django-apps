from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome_view(request):
    print('This line added by view function')
    return HttpResponse('<h1>Custom Middleware Demo</h1>')
def home_page_view(request):
    return HttpResponse('<h1>Hello this is from Home page</h1>')
def home_page_view2(request):
    print(10/0)
    return HttpResponse('<h1>Hello this is from Home page</h1>')
def home_page_view3(request):
    print('this line printed by view function')
    return HttpResponse('<h1>Hello this is from first and second middleware page view</h1>')    
