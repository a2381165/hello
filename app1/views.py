from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse,Http404
from .models import User,Diary
from django.shortcuts import render_to_response,render,redirect,reverse,HttpResponseRedirect,get_object_or_404
from django.template import Context,loader
from django.forms.models import model_to_dict
import time
# 接收请求数据返回字符串响应。http://127.0.0.1:8000/app1/
def index(request):
    return HttpResponse("Hello, world") # 直接返回响应字符串
# 返回字典或json字符串
def finduser(request):
    try:
        userid = request.GET.get("userid", None) # 读取数据
        users = User.objects.filter(id=userid) # 获取一个用户，返回QuerySet
        user = users[0] # 获取第一个user对象
        user_dict1 = model_to_dict(user) # 将对象转化为字典
        return JsonResponse(user_dict1) # 返回前端字典
    except:
        raise Http404("用户不存在")
