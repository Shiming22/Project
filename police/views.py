from django.shortcuts import render  # 导入render模块

def index(request):
    views_name="菜鸟"
    return render(request,'index.html', {"name":views_name})
